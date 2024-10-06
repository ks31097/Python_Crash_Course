class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name, self.last_name, self.age, self.country)

    def greet_user(self):
        message = f"Hello, {self.first_name}!"
        return message
    
    def login_info(self):
        print(self.login_attempts)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        answer = input("Do you want reset login attemps? ")
        if answer.lower() == 'yes':
            self.login_attempts = 0
        else:
            print("The operation was stopped!")
    
# user = User(1, 2, 3, 4)

# user.describe_user()
# print(type(user))
# print(type(user.greet_user()))
# print(type(user.describe_user()))
# print(user.greet_user())
# user.login_info()

# for _ in range(3):
#     user.increment_login_attempts()

# user.login_info()
# user.reset_login_attempts()
# user.login_info()


class Privileges():
    def __init__(self, *admin_privileges):
        self.privileges = admin_privileges

    def show_privileges(self):
        print("Admin privileges: ")
        for privilege in self.privileges:
            print(f"\t {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.orivileges = Privileges(1, 2, 3)

# super_admin = Admin('name', 'soname', 19, 'ukraine')
# print(super_admin.last_name)

# super_admin.orivileges.show_privileges()