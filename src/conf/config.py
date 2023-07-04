from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str = 'postgresql+psycopg2://user:password@localhost:5432/postgres'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
