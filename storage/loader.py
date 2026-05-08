import json

def load_users():
    with open("data/users.json", "r") as file:
        data = json.load(file)

    return data
