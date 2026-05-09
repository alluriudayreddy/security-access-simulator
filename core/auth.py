from storage.loader import load_users

def login(username, password):
    data = load_users()

    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            return user 
        
    return None
    