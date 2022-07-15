from pony.orm import PrimaryKey, Required

from models.base_model import db


# class Profile(db.Entity):
#     _table_ = "profiles"
#     id = PrimaryKey(str, 10)
#     type = Required(str, 25)
#     user = Required('User', column='user_id')
#     # can be used like foreign key
#     # user_id = ForeignKey()
