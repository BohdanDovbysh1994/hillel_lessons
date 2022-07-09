from sqlalchemy.orm import declarative_base
from sqlalchemy import INTEGER, Column, VARCHAR

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(25))
    age = Column(INTEGER)
    email = Column(VARCHAR(25))

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, age: {self.age}, email: {self.email}'
