import copy
import datetime

from fastapi.testclient import TestClient
from datetime import date

from app.main import app


client = TestClient(app)


def test_create_new_todo():
    todo_data = {
        "id": 1,
        "todo_name": "test name",
        "description": "test desc",
        "end_date": date.today().isoformat(),
        "important": False,
    }

    response = client.post(url="/todo/new-todo/", json=todo_data)
    assert response.status_code == 200
    assert response.json() == todo_data
