import json
"""The program loads the username if it was saved earlier."""
""""Otherwise, it prompts for the username and saves it"""

def checked_the_name(username):
    print(f"Your name is {username}?")
    user_answer = input("Input \"yes\" or \"No\": ")
    if user_answer.lower().strip() == "yes":
        return username
    else:
        return None

def get_stored_username():
    """Gets the stored username, if it exists."""
    filename = "json/my_username_new.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Requests a new username"""
    username = input("What is your name? ")
    filename = 'json/my_username_new.json'
    with open(filename, 'w') as f:
        json.dump(username, f)

    return username
        
def greet_user():
    """Greets the user by name."""
    username = get_stored_username()

    if checked_the_name(username):
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()