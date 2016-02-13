import json


# def greet_user():
#     """Greet the user by name."""
#
#     # Load the username, if it has been stored previously.
#     # Otherwise, prompt for the username and store it.
#
#     filename = "username.json"
#
#     try:
#         with open(filename) as file_object:
#             username = json.load(file_object)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, "w") as file_object:
#             json.dump(username, file_object)
#             print("We\'ll remember you when you come back, " + username +
#                   "!")
#     else:
#         print("Welcome back, " + username + "!")
#
# greet_user()

def get_stored_username():
    """Get stored username if available."""
    filename = "username.json"

    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = "username.json"

    with open(filename, "w") as file_object:
        json.dump(username, file_object)

    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We\'ll remember you when you come back, " + username + "!")

greet_user()
