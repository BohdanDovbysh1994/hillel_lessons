from pony.orm import Database, sql_debug
from pony.orm import PrimaryKey, Required, Set

db = Database()

db.bind('postgres', user='postgres', password='123', host='localhost', database='testdb')


class User(db.Entity):
    _table_ = "users"
    id = PrimaryKey(int, auto=True)
    name = Required(str, 25)
    age = Required(int)
    email = Required(str, 25, unique=True)
    profiles = Set('Profile')

    def to_dict_with_profile(self):
        data = {}
        for key, value in self._vals_.items():
            data[key.name] = value
        data['profiles'] = []
        for profile in self.profiles:
            data['profiles'].append(profile.to_dict())
        return data

    def to_dict(self):
        data = {}
        for key, value in self._vals_.items():
            data[key.name] = value
        return data


class Profile(db.Entity):
    _table_ = "profiles"
    id = PrimaryKey(str, 10)
    type = Required(str, 25)
    user = Required('User', column='user_id')

    # def __str__(self):
    #     pass

    def to_dict(self):
        data = {}
        for key, value in self._vals_.items():
            name = key.name
            if name == 'user':
                continue
            data[name] = value
        return data


# sql_debug(True)
db.generate_mapping(create_tables=True)
