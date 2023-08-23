import logging
from typing import List, Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = "local"
    LOG_LEVEL: int = logging.INFO
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"
    API_PREFIX: str = "/api"
    # default origins: angular/nuxt
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:5174"]
    SQLALCHEMY_DATABASE_URI: str = (
        "postgresql://postgres:postgres@localhost:5432/minseed"
    )
    MAX_PAGE_SIZE: int = 100
    LOG_NAME: str = "minseed"
    PROJECT_ID: Optional[str]
    PROJECT_NUMBER: Optional[str]
    LOCAL_EMAIL_ADMIN = "iapPrenom.iapNom@gmail.com"

    class Config:
        env_file = ".env"


settings = Settings()
