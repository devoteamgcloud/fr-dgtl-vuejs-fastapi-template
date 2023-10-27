import logging
from typing import List, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "local"
    LOG_LEVEL: int = logging.INFO
    PROJECT_NAME: str = "FastApi template"
    API_PREFIX: str = "/api"
    # default origins: angular/nuxt
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:5174"]
    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:postgres@localhost:5432/minseed"
    MAX_PAGE_SIZE: int = 100
    LOG_NAME: str = "minseed"
    PROJECT_ID: Optional[str] = None
    PROJECT_NUMBER: Optional[str] = None
    LOCAL_EMAIL_ADMIN: str = "iapPrenom.iapNom@gmail.com"

    class Config:
        env_file = ".env"


settings = Settings()
