class Emlpoyee():
    def __init__(self, first_name, second_name, year_salary):
        self.first_name = first_name
        self.second_name = second_name
        self.year_salary = int(year_salary)
    
    def information_about_the_employee(self):
        return f"The employee full name: {self.first_name} {self.second_name} - year salary: {self.year_salary}"
    
    def give_raise(self, raise_of_the_year_salary=5000):
        emlpoyee_year_salary = self.year_salary + raise_of_the_year_salary
        return f"Your year salary rise is: {raise_of_the_year_salary}, your year salary is: {emlpoyee_year_salary}"