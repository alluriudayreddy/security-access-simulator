from storage.loader import load_users

def get_all_users():
    data = load_users()
    return data["users"]

def find_user(username):
    users = get_all_users()

    for user in users:
        if user["username"] == username:
            return user
    
    return None