from os import path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_url: str = f"sqlite+aiosqlite:///./app/db/todo.db"
    db_echo: bool = True


settings = Settings()
