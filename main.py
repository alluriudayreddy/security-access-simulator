from core.auth import login
from core.session import set_current_user, logout
from core.permissions import has_permission
from core.user_manager import add_user, view_all_users, delete_user

from utils.validators import validate_username, validate_password
from utils.helpers import print_separator, format_username
from utils.logger import log_info, log_warning, log_error

from interface.menu import show_main_menu, show_admin_menu

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


while True:

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
            print(INVALID_USERNAME)
            print_separator()
            continue

        if not validate_password(password):
            print_separator()
            log_error("Invalid password entered.")
            print(INVALID_PASSWORD)
            print_separator()
            continue


        user = login(username, password)


        if user:

            set_current_user(user)

            log_info(f"{user['username']} logged in successfully")

            print_separator()

            print(f"{WELCOME_MESSAGE} {user['username']}")

            print_separator()


            if has_permission(user, "admin"):

                print(ADMIN_ACCESS)

                log_info(f"Admin access granted to {user['username']}")

                print_separator()

                show_admin_menu()

                admin_choice = input("Choose admin option: ")

                print_separator()


                if admin_choice == "1":

                    users = view_all_users()

                    for user_data in users:
                        print(f"{user_data['username']} - {user_data['role']}")

                    print_separator()


                elif admin_choice == "2":

                    delete_username = input("Enter username to delete: ")

                    result = delete_user(delete_username)

                    print_separator()

                    if result:
                        print("User deleted successfully.")

                    else:
                        print("User not found.")

                    print_separator()


                elif admin_choice == "3":

                    update_username = input("Enter username: ")
                    new_password = input("Enter new password: ")

                    print_separator()
                    print("Password update feature coming soon.")
                    print_separator()


                elif admin_choice == "4":

                    search_username = input("Enter username to search: ")

                    print_separator()
                    print("Search user feature coming soon.")
                    print_separator()


                elif admin_choice == "5":

                    logout()

                    print_separator()
                    print("Admin logged out successfully.")
                    print_separator()


                elif admin_choice == "6":

                    print_separator()
                    print("Exiting admin panel.")
                    print_separator()


                else:

                    print_separator()
                    print("Invalid admin option.")
                    print_separator()


            else:

                log_warning(f"Normal user access granted to {user['username']}")

                print(USER_ACCESS)

                print_separator()


        else:

            print_separator()

            log_error("Invalid username or password.")

            print(INVALID_CREDENTIALS)

            print_separator()


    elif choice == "2":

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        username = format_username(username)

        if not validate_username(username):
            print_separator()
            log_error("Invalid username entered.")
            print(INVALID_USERNAME)
            print_separator()
            continue

        if not validate_password(password):
            print_separator()
            log_error("Invalid password entered.")
            print(INVALID_PASSWORD)
            print_separator()
            continue


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

        break


    elif choice == "4":

        logout()

        print_separator()

        print("Logged out successfully.")

        print_separator()


    else:

        print_separator()

        print(INVALID_CHOICE)

        print_separator()