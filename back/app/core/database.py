from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import env

Base = declarative_base()

engine=create_engine(
    env.DATABASE_URL,
    echo=False,
    pool_logging_name=True
)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()


