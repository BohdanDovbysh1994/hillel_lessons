from pony.orm import PrimaryKey, Required, Set
from models.base_model import db


# class User(db.Entity):
#     _table_ = "users"
#     id = PrimaryKey(int, auto=True)
#     name = Required(str, 25)
#     age = Required(int)
#     email = Required(str, 25, unique=True)
#     profiles = Set('Profile')
