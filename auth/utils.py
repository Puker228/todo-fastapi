import jwt
from datetime import timedelta, datetime, UTC


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=30)
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode, 'asdasd', 'HS256')
    return encoded_jwt


print(create_access_token({'ya': 'ne ya'}))