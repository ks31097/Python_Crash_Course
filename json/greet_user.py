import json

filename = 'json/username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    print(f"File \"{filename}\" is not exist!")
else:
    print(f"Welcome back, {username}!")