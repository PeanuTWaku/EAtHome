from pydantic import BaseSettings, Field


class DatabaseSettings(BaseSettings):
    """Settings for database."""

    DB_DRIVER: str = Field(default="postgresql+asyncpg", env="DB_DRIVER")
    DB_HOST: str = Field(default="localhost", env="DB_HOST")
    DB_USER: str = Field(default="postgres", env="DB_USER")
    DB_PASSWORD: str = Field(default="changeme", env="DB_PASSWORD")
    DB_NAME: str = Field(default="postgres", env="DB_NAME")


class AuthSettings(BaseSettings):
    """Settings for authentication."""

    SECRET_KEY: str = Field(default="dev", env="FASTAPI_AUTH_SECRET_KEY")
    TOKEN_URL: str = Field(default="/login", env="FASTAPI_TOKEN_URL")


class APISettings(BaseSettings):
    """Settings for API routes."""

    API_V1_URL: str = Field(default="/api/v1", env="FASTAPI_API_V1_URL")


class Settings(DatabaseSettings, AuthSettings, APISettings):
    """Settings for whole application."""

    class Config:
        env_file = ".env"


settings = Settings()
