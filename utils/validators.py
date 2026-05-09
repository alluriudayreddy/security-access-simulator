def validate_username(username):
    return len(username.strip()) > 0

def validate_password(password):
    return len(password) >= 6