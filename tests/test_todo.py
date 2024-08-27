# from fastapi.testclient import TestClient
# from datetime import date
#
# from app.main import app
#
#
# client = TestClient(app)
#
#
# def test_create_new_todo():
#     todo_data = {
#         "todo_name": "test name",
#         "description": "test desc",
#         "end_date": date.today().isoformat(),
#         "important": False,
#     }
#
#     todo_response = todo_data.copy()
#     todo_response["id"] = 1
#
#     response = client.post(url="/todo/new-todo/", json=todo_data)
#     assert response.status_code == 200
#     assert response.json() == todo_response
#
#
# def test_create_new_todo_bad_data():
#     todo_data = {
#         "id": 1,
#         "todo_name": "Puking",
#         "description": 228,
#         "end_date": date.today().isoformat(),
#         "important": False,
#     }
#
#     response_detail = {
#         "detail": [
#             {
#                 "input": 228,
#                 "loc": [
#                     "body",
#                     "description",
#                 ],
#                 "msg": "Input should be a valid string",
#                 "type": "string_type",
#             },
#         ],
#     }
#
#     response = client.post(url="/todo/new-todo/", json=todo_data)
#     assert response.status_code == 422
#     assert response.json() == response_detail
