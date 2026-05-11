from storage.loader import load_users

failed_attempts = 0
MAX_ATTEMPTS = 3

def login(username, password):
    global failed_attempts

    data =  load_users()

    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            failed_attempts = 0

            return user
        
    failed_attempts += 1

    return None
