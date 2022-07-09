from sqlalchemy import create_engine, Column, INTEGER, VARCHAR
from sqlalchemy.orm import sessionmaker, declarative_base, Session

engine = create_engine("postgresql://postgres:123@localhost/testdb")

__session = sessionmaker(engine)

session: Session = __session()
