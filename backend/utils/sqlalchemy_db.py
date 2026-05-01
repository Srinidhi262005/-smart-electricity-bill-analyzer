import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.config import Config
from models.base import Base


def get_sqlalchemy_url(db_path):
    return f"sqlite:///{db_path}"


def get_engine(db_path=None):
    if db_path is None:
        db_path = Config.DATABASE_PATH
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return create_engine(get_sqlalchemy_url(db_path), connect_args={'check_same_thread': False})


def get_session_factory(engine=None):
    if engine is None:
        engine = get_engine()
    return sessionmaker(bind=engine)


def init_sqlalchemy_db(db_path=None):
    engine = get_engine(db_path)
    Base.metadata.create_all(engine)
    return engine
