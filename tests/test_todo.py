from fastapi.testclient import TestClient
from datetime import date

from app.main import app


client = TestClient(app)


def test_create_new_todo():
    todo_data = {
        "todo_name": "Test ToDo",
        "description": "This is a test task.",
        "end_date": date.today().isoformat(),
        "important": True,
    }

    response = client.post(url="/todo/new-todo/", json=todo_data)
    assert response.status_code == 200
    assert response.json() == todo_data
