import json

def save_users(data):
    try:
        with open("data/users.json", "w") as file:
            json.dump(data, file, indent=4)

    except Exception:
        print("Error saving users data.")