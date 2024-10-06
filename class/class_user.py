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