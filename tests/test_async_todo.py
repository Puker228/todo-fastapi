import pytest

from httpx import AsyncClient, ASGITransport
from datetime import date

from app.main import app


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}


@pytest.mark.anyio
async def test_post_new_todo():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        todo_data = {
            "todo_name": "test name 1",
            "description": "test desc 1",
            "end_date": date.today().isoformat(),
            "important": True,
        }

        todo_response = todo_data.copy()
        todo_response["id"] = 1

        response = await ac.post(url="/todo/new-todo/", json=todo_data)
    assert response.status_code == 200
    assert response.json() == todo_response
