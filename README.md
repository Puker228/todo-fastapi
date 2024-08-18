# todo-fastapi

## install requirements
```
python3.11 -m venv .venv
source .venv/bin/activate
pip3.11 install -r requirements.txt
```

## run server
```
uvicorn app.main:app --reload
```

## env переменыне 
| переменная |         значение         |
| :--------: | :----------------------: |
|  DB_HOST   |  строка, название хоста  |
|  DB_PORT   |       число, порт        |
|  DB_USER   | строка, имя пользователя |
|  DB_PASS   |   строка, пароль от бд   |
|  DB_NAME   |   строка, название бд    |
