# pr_fast_api_todos

A FastAPI-based TODO application with user authentication and task management.

## What this project contains

- **FastAPI application** with user authentication and TODO management features
- **Core code** in the `TodoApp` package:
    - `main.py` - Application entry point
    - `models.py` - SQLAlchemy ORM models for Users and Todos
    - `database.py` - Database configuration and session management
    - `routers/auth.py` - User authentication endpoints
    - `routers/todos.py` - TODO operations endpoints
- **SQLite database** for persistent data storage
- `requirements.txt` with project dependencies

## Features Implemented

### Authentication Module (`routers/auth.py`)

- User registration endpoint (`POST /auth`)
- User credentials management with bcrypt password hashing
- Password verification and authentication logic
- Support for user roles and profile information

### TODO Management Module (`routers/todos.py`)

- **Get all TODOs** - `GET /` - Retrieve all TODO items
- **Get single TODO** - `GET /todo/{todo_id}` - Retrieve a specific TODO by ID
- **Create TODO** - `POST /todo` - Create a new TODO item
- **Update TODO** - `PUT /todo/{todo_id}` - Update an existing TODO
- Data validation with Pydantic models (title, description, priority, completion status)
- RESTful API with proper HTTP status codes

### Data Models

- **Users Table**: id, email, username, first_name, last_name, hashed_password, is_active, role
- **Todos Table**: id, title, description, priority, complete, owner_id (foreign key to users)

### Database

- SQLite database with SQLAlchemy ORM
- Automatic table creation on app startup
- Session management with proper dependency injection

## Quick start

1. Install dependencies:

    ```
    pip install -r TodoApp/requirements.txt
    ```

2. Run the app (development):

    ```
    uvicorn TodoApp.main:app --reload
    ```

3. Access the API documentation:
    - Swagger UI: `http://localhost:8000/docs`
    - ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
TodoApp/
├── __init__.py
├── main.py              # FastAPI application setup
├── models.py            # SQLAlchemy models (Users, Todos)
├── database.py          # Database configuration
├── requirements.txt     # Python dependencies
└── routers/
    ├── __init__.py
    ├── auth.py          # Authentication routes
    └── todos.py         # TODO management routes
```

## License

This project is provided as-is for learning and demonstration purposes.
