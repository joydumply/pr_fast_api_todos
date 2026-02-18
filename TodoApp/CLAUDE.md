# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the App

```bash
uvicorn main:app --reload
```

Interactive API docs are available at `http://127.0.0.1:8000/docs` once running.

## Installing Dependencies

```bash
pip install -r requirements.txt
# Additional packages required but not in requirements.txt:
pip install passlib[bcrypt] python-jose[cryptography] psycopg2-binary
```

## Architecture

The app is a FastAPI backend with four routers mounted in `main.py`:

- `routers/auth.py` — `/auth` prefix: user registration (`POST /auth/`) and login (`POST /auth/token`). Defines `get_current_user()` which all other routers import to enforce authentication via JWT.
- `routers/todos.py` — no prefix: CRUD for todos, scoped to the authenticated user via `owner_id`.
- `routers/admin.py` — `/admin` prefix: admin-only endpoints (get all todos, delete any todo). Role is checked from the JWT payload (`user_role == 'admin'`).
- `routers/users.py` — `/users` prefix: get own profile, change password.

**Database** (`database.py`): SQLAlchemy with PostgreSQL. The connection string is hardcoded. Tables are auto-created on startup via `models.Base.metadata.create_all(bind=engine)` in `main.py`.

**Models** (`models.py`): `Users` and `Todos`. `Todos.owner_id` is a FK to `Users.id`.

**Auth flow**: JWT tokens are issued at `/auth/token` (OAuth2 password flow). `get_current_user()` in `routers/auth.py` decodes the token and returns `{'username', 'id', 'user_role'}`. All protected routes declare `user_dependency = Annotated[dict, Depends(get_current_user)]`.

**`get_db()`** is duplicated in each router file — each defines its own session dependency rather than sharing one from a common module.

## Database

PostgreSQL database: `todoapplicationdatabase`. Connection string is set directly in `database.py`. There is also a leftover `todos_app.db` SQLite file from an earlier development phase — it is unused.
