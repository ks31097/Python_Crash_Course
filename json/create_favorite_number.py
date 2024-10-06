import json
"""The program loads the favorite user number if it was saved earlier."""
""""Otherwise, it prompts for the favorite user number and saves it"""

def get_stored_favorite_number():
    """Get the stored user favorite number, if it exist."""
    filename = 'json/user_favorite_number.json'

    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number
    
def get_new_favorite_number():
    """Request a new favorite number"""
    favorite_number = input("What is your favorite number? ")
    filename = 'json/user_favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)

    return favorite_number

def show_favorite_number():
    """Show the user favorite number"""
    favorite_number = get_stored_favorite_number()
    if favorite_number:
        print(f"Your favorite number: {favorite_number}")
    else:
        favorite_number = get_new_favorite_number()
        print(f"We'll remember your favorite number for next time, {favorite_number}")

show_favorite_number()