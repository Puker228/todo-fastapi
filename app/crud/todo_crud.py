from app.crud.base_crud import BaseCRUD
from app.models.todo_models import ToDo


class ToDoCRUD(BaseCRUD):
    model = ToDo
