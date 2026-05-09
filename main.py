from core.auth import login
from core.session import set_current_user
from core.permissions import has_permission

from utils.validators import validate_username, validate_password
from utils.helpers import print_separator, format_username

print_separator()

username = input("Enter Username: ")
password = input("Enter Password: ")

username = format_username(username)


if not validate_username(username):
    print_separator()
    print("Invalid username.")
    print_separator()
    exit()

if not validate_password(password):
    print_separator()
    print("Invalid password.")
    print_separator()
    exit()


    user = login(username, password)


if user:
    set_current_user(user)

    print_separator()

    print(f"Welcome {user['username']}")

    print_separator()

    if has_permission(user, "admin"):
        print("Admin access granted.")
    else:
        print("Normal user access granted.")

    print_separator()

else:
    print_separator()
    print("Invalid username or password.")
    print_separator()