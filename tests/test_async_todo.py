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
            "todo_name": "test name",
            "description": "test desc",
            "end_date": date.today().isoformat(),
            "important": True,
        }

        todo_response = todo_data.copy()
        todo_response["id"] = 1

        response = await ac.post(url="/todo/new-todo/", json=todo_data)
    assert response.status_code == 200
    assert response.json() == todo_response


@pytest.mark.anyio
async def test_create_new_todo_bad_data():
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        todo_data = {
            "id": 1,
            "todo_name": "Puking",
            "description": 228,
            "end_date": date.today().isoformat(),
            "important": False,
        }

        response_detail = {
            "detail": [
                {
                    "input": 228,
                    "loc": [
                        "body",
                        "description",
                    ],
                    "msg": "Input should be a valid string",
                    "type": "string_type",
                },
            ],
        }

        response = await ac.post(url="/todo/new-todo/", json=todo_data)
    assert response.status_code == 422
    assert response.json() == response_detail
