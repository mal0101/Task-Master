# Task Master - Flask Backend Learning Project

A simple Flask todo application built to learn backend development with Python. This project focuses on understanding Flask fundamentals, SQLAlchemy ORM, and basic CRUD operations with minimal frontend styling.

## Learning Objectives

This project was created to understand:
- 🐍 Flask application structure and routing
- 🗄️ SQLAlchemy ORM and database operations
- 🔄 CRUD operations (Create, Read, Update, Delete)
- 📝 HTML templating with Jinja2
- 🌐 HTTP methods (GET, POST)
- 📊 Database relationships and models

## Features

**Backend Functionality:**
- RESTful routes for task management
- SQLite database integration with SQLAlchemy
- Database model definition and relationships
- Form handling and data validation
- Error handling for database operations

**Basic Frontend:**
- Simple HTML templates for functionality testing
- Basic CSS for minimal styling
- Form inputs for task management

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Templates**: Jinja2 templating engine
- **Frontend**: Basic HTML/CSS (minimal styling)

## Project Structure

```
flask-todo-backend/
├── app.py                 # Main Flask application & routes
├── requirements.txt       # Python dependencies
├── static/
│   └── css/
│       └── main.css       # Basic styling
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Main page
│   └── edit.html          # Edit form
└── README.md
```

## Backend Architecture
The Flask application follows a simple MVC pattern:

**Application Structure:**
- **Models**: SQLAlchemy classes define database schema
- **Views**: Route functions handle HTTP requests/responses  
- **Templates**: Jinja2 templates render HTML with dynamic content

**Core Components:**
- **Flask App Instance**: Manages configuration and request handling
- **SQLAlchemy Database**: ORM for database operations
- **Route Handlers**: Functions mapped to URL endpoints
- **Template Engine**: Renders dynamic HTML responses

**Request Flow:**
1. Client sends HTTP request to Flask route
2. Route function processes request data
3. Database operations via SQLAlchemy models
4. Template renders with context data
5. HTML response sent back to client
### Database Model
```python
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
```

### API Routes
- `GET /` - Display all tasks
- `POST /` - Create new task
- `GET /edit/<id>` - Show edit form
- `POST /edit/<id>` - Update task
- `GET /delete/<id>` - Delete task

## Installation & Setup

### Prerequisites
- Python 3.7+
- Basic understanding of Flask concepts

### Setup Instructions

1. **Clone and navigate to project**
   ```bash
   git clone <repository-url>
   cd flask-todo-backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**
   
   Uncomment these lines in `app.py` for first run:
   ```python
   if __name__ == '__main__':
       with app.app_context():
           db.create_all()
       app.run(debug=True)
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Test the backend**
   
   Visit `http://localhost:5000` to test CRUD operations

## Key Learning Concepts Demonstrated

### 1. Flask Application Setup
- Application factory pattern basics
- Configuration management
- Debug mode setup

### 2. Database Integration
- SQLAlchemy ORM setup
- Model definition and relationships
- Database initialization
- CRUD operations with try/catch error handling

### 3. Routing and HTTP Methods
- Route decorators with multiple HTTP methods
- URL parameters for dynamic routes
- Request data handling (forms)

### 4. Template Integration
- Jinja2 template inheritance
- Template context passing
- Basic template logic (loops, conditionals)

## Backend Testing

Test the following functionality:

**Create Task:**
```bash
curl -X POST http://localhost:5000/ -d "task=Learn Flask" -H "Content-Type: application/x-www-form-urlencoded"
```

**View Tasks:**
```bash
curl http://localhost:5000/
```

## Database Operations

The application demonstrates:
- **Create**: Adding new tasks via POST request
- **Read**: Querying and displaying all tasks
- **Update**: Editing existing task content
- **Delete**: Removing tasks by ID

Database file (`test.db`) is created automatically on first run.

## Next Steps for Learning

**Backend Enhancements:**
- [ ] Add REST API endpoints (JSON responses)
- [ ] Implement user authentication
- [ ] Add input validation and sanitization
- [ ] Create database migrations
- [ ] Add logging and monitoring
- [ ] Implement task completion status
- [ ] Add API documentation (Swagger)

**Frontend Improvements:**
- [ ] Modern CSS framework (Bootstrap/Tailwind)
- [ ] JavaScript for dynamic interactions
- [ ] AJAX requests for seamless UX
- [ ] Form validation on frontend

## Dependencies

Key Flask packages used:
- `Flask==3.0.3` - Core web framework
- `Flask-SQLAlchemy==3.1.1` - Database ORM
- `gunicorn==23.0.0` - Production WSGI server

## Development Notes

- Database models are simple for learning purposes
- Error handling is basic but functional
- Templates are minimal - focus is on backend logic
- Debug mode enabled for development learning

## License

MIT License - Feel free to use for learning purposes

---

**This is a learning project focused on Flask backend development fundamentals** 🎓