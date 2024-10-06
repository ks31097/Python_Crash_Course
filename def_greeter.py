username = "kostiantyn"

def greet_user(username):
    print(f"Hello, {username.title()}!")

run_code = 1
while run_code <= 5:
    greet_user(username)
    run_code += 1

print("")

run_code = 1
while run_code <= 5:
    greet_user('user')
    run_code += 1