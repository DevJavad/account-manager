from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    ADMIN: str
    DB_URL: str
    API_ID: int
    API_HASH: str

    class Config:
        env_file = ".env"


settings = Settings()