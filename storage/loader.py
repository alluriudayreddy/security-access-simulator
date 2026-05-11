import json

def load_users():
    try:
        with open("data/users.json", "r") as file:
            data = json.load(file)

            return data
    
    except FileNotFoundError:
        print("Users file not found.")

        return {"users": []}
    
    except json.JSONDecodeError:
        print("Invalid JSON data.")

        return {"users": []}
