from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # DB_HOST: str
    # DB_PORT: int
    # DB_USER: str
    # DB_PASS: str
    # DB_NAME: str

    @property
    def SQLITE_URL(self):
        return f"sqlite+aiosqlite:///app/db/todo.db"

    # model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
