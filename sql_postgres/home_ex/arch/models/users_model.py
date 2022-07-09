from sqlalchemy import create_engine, Column, INTEGER, VARCHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(25))
    age = Column(INTEGER)
    email = Column(VARCHAR(25))

    def __str__(self):
        return f"id: {self.id}, 'name': {self.name}, 'age': {self.age}, 'email': {self.email}"
