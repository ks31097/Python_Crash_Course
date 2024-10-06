from class_user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age=0, country='Add a country'):
        super().__init__(first_name, last_name, age, country)
        self.orivileges = Privileges(1, 2, 3)