from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    username = Column('username', String(50), nullable=False)
    created_at = Column('created_at', DateTime, nullable=False, default=datetime.now())


class Media(Base):
    """
        Media.status "LIKED"|"ERROR"
    """
    __tablename__ = 'media'
    created_at = Column('created_at', DateTime, nullable=False, default=datetime.now())
    status = Column('string', String(20), nullable=False)
