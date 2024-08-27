from crud.base import BaseCRUD
from todo.models import ToDo


class ToDoCRUD(BaseCRUD):
    model = ToDo
