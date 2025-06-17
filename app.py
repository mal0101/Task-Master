from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app) # Initialize the database

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def __repr__(self):
        return '<Task %r>' % self.id  # Returns a task with its ID
    
@app.route('/', methods = ['POST', 'GET']) 


def index():
    if request.method == 'POST':
        task_content = request.form["task"]
        new_task = Todo(content = task_content)
        try:
            db.session.add(new_task)  
            db.session.commit() 
            return redirect('/')
        except:
            return "There was an issue adding your task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # .first() returns the first task
        return render_template('index.html', tasks= tasks)
  
@app.route('/delete/<int:id>')  
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that task"

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['task']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your task"
    else:
        return render_template('edit.html', task=task)

if __name__ == '__main__':
    # with app.app_context(): # to start the database 
        # db.create_all()
    app.run(debug = True)