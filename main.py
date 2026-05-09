from core.auth import login
from core.session import set_current_user
from core.permissions import has_permission
from utils.validators import validate_username, validate_password


username = input("Enter Username: ")
password = input("Enter Password: ")


if not validate_username(username):
    print("Invalid username.")
    exit()

if not validate_password(password):
    print("Invalid password.")
    exit()


    user = login(username, password)


if user:
    set_current_user(user)
    print(f"Welcome {user['username']}")

    if has_permission(user, "admin"):
        print("Admin access granted.")
    else:
        print("Normal user access granted.")

else:
    print("Invalid username or password.")
    
