import json

def save_users(data):
    with open("data/users.json", "w") as file:
        json.dump(data, file, indent=4)