from storage.loader import load_users
from storage.saver import save_users

def get_all_users():
    data = load_users()
    return data["users"]


def find_user(username):
    users = get_all_users()

    for user in users:
        if user["username"] == username:
            return user
    
    return None


def add_user(username, password, role):
    data = load_users()

    for user in data["users"]:
        if user["username"] == username:
            return False

    new_user = {
        "username": username,
        "password": password,
        "role": role
    }

    data["users"].append(new_user)
    save_users(data)

    return True


def view_all_users():
    users = get_all_users()

    return users


def delete_user(username):
    users = get_all_users()

    for user in users:
        if user["username"] == username:
            users.remove(user)

            data = {
                "users": users
            }
            save_users(data)

            return True
        return False
    

def update_user_password(username, new_password):
    users = get_all_users()

    for user in users:
        if user["username"] == username:

            user["password"] = new_password

            data = {
                "users": users
            }

            save_users(data)

            return True

    return False


def search_user(username):
    users = get_all_users()

    for user in users:
        if user["username"] == username:
            return user

    return None