from app.schemas.user_schema import SUser
from auth import utils as auth_utils


john = SUser(
    username='cool',
    password=auth_utils.hashed_password('qwerty2323'),
    email='hhhhh@mail.com'
)

denis = SUser(
    username='cool22222',
    password=auth_utils.hashed_password('secrt'),
)


users_db: dict[str, SUser] = {
    john.username: john,
    denis.username: denis
}