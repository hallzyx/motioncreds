from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from app.core.database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(50),nullable=False)
    email=Column(String(50), unique=True,index=True, nullable=False)
    gesture_data = Column(JSON, nullable=True)