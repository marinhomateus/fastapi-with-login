from sqlmodel import SQLModel, Session, create_engine
from pydantic import BaseSettings, Field
from ..models import models

sqlite_file_name = "database.db"


class Settings(BaseSettings):
    db_user: str = Field(..., env="POSTGRES_USER")
    db_password: str = Field(..., env="POSTGRES_PASSWORD")
    db_host: str = Field(..., env="POSTGRES_HOST")
    db_port: str = Field(..., env="POSTGRES_PORT")
    db_name: str = Field(..., env="POSTGRES_DB")

    class Config:
        env_file = "database.conf"


settings = Settings()

engine = create_engine(
    f"postgresql+psycopg2://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
)


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)
