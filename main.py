from core.auth import login
from core.session import set_current_user
from core.permissions import has_permission
from core.user_manager import add_user

from utils.validators import validate_username, validate_password
from utils.helpers import print_separator, format_username
from utils.logger import log_info, log_warning, log_error


print_separator()

choice = input("Choose option (login/register): ").lower()

print_separator()


if choice == "register":

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    username = format_username(username)

    if not validate_username(username):
        print_separator()
        log_error("Invalid username entered.")
        print_separator()
        exit()

    if not validate_password(password):
        print_separator()
        log_error("Invalid password entered.")
        print_separator()
        exit()

    add_user(username, password, "user")

    log_info(f"New user registered: {username}")

    print_separator()
    print("User registered successfully.")
    print_separator()


elif choice == "login":

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    username = format_username(username)

    if not validate_username(username):
        print_separator()
        log_error("Invalid username entered.")
        print_separator()
        exit()

    if not validate_password(password):
        print_separator()
        log_error("Invalid password entered.")
        print_separator()
        exit()

    user = login(username, password)

    if user:
        set_current_user(user)

        log_info(f"{user['username']} logged in successfully")

        print_separator()

        print(f"Welcome {user['username']}")

        print_separator()

        if has_permission(user, "admin"):
            log_info(f"Admin access granted to {user['username']}")

        else:
            log_warning(f"Normal user access granted to {user['username']}")

        print_separator()

    else:
        print_separator()
        log_error("Invalid username or password.")
        print_separator()


else:
    print_separator()
    print("Invalid option selected.")
    print_separator()