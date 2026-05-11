from core.auth import login
from core.session import set_current_user
from core.permissions import has_permission
from core.user_manager import add_user

from utils.validators import validate_username, validate_password
from utils.helpers import print_separator, format_username
from utils.logger import log_info, log_warning, log_error

from interface.menu import show_main_menu

from interface.messages import (
    INVALID_USERNAME,
    INVALID_PASSWORD,
    INVALID_CREDENTIALS,
    WELCOME_MESSAGE,
    ADMIN_ACCESS,
    USER_ACCESS,
    REGISTER_SUCCESS,
    EXIT_MESSAGE,
    INVALID_CHOICE
)


print_separator()

show_main_menu()

print_separator()

choice = input("Choose option: ")

print_separator()


if choice == "1":

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

        print(f"{WELCOME_MESSAGE} {user['username']}")

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


elif choice == "2":

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

    result = add_user(username, password, "user")
    if result:
        log_info(f"New user registered: {username}")

        print_separator()
        print(REGISTER_SUCCESS)
        print_separator()
    
    else:
        print_separator()
        print("User already exists.")
        print_separator()


elif choice == "3":

    print_separator()
    print(EXIT_MESSAGE)
    print_separator()


else:

    print_separator()
    print(INVALID_CHOICE)
    print_separator()