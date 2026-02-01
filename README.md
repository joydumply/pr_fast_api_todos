# pr_fast_api_todos

A minimal FastAPI-based TODO application.

What this project contains

- A simple FastAPI app that manages TODO items.
- Core code in the `TodoApp` package: `main.py`, `models.py`, and `database.py`.
- A `requirements.txt` with the project's Python dependencies.

Quick start

1. Install dependencies:

    pip install -r TodoApp/requirements.txt

2. Run the app (development):

    uvicorn TodoApp.main:app --reload

What was done

- Implemented a REST API for basic TODO operations (create/read/update/delete).
- Organized code into a small package with clear separation of models and DB logic.

License
This project is provided as-is for learning and demonstration purposes.
