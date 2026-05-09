from core.auth import login
from core.session import set_current_user
from core.permissions import has_permission

username = input("Enter Username: ")
password = input("Enter Password: ")

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
    