from class_employee import Emlpoyee

first_employee = Emlpoyee('First name', 'Second name', 5000)

print(first_employee.information_about_the_employee())
print(first_employee.give_raise())
print(first_employee.give_raise(10000))