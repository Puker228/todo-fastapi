from app.crud.base import BaseCRUD
from app.models.todo import ToDo


class ToDoCRUD(BaseCRUD):
    model = ToDo
