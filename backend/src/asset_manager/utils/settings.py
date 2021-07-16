from pydantic import BaseSettings


class Settings(BaseSettings):
    CONNECTION_STRING: str
    DATABASE_NAME: str

    class Config:
        env_file = ".env"
