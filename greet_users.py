def greet_users(names):
    """Output a welcome message for each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
    
usernames = ['hannah', 'try', 'margot']
greet_users(usernames)