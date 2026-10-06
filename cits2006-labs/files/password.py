import getpass

database = {"user1": "123456", "user2": "654321"}
MAX_ATTEMPTS = 3


def check(username: str, password: str) -> bool:
    """True only if the user exists and the password matches."""
    return username in database and database[username] == password


if __name__ == '__main__':
    username = input("Enter Your Username : ")
    for _ in range(MAX_ATTEMPTS):
        if check(username, getpass.getpass("Enter Your Password : ")):
            print("Authenticated!")
            break
        print("Wrong username or password.")
    else:
        print("Too many attempts.")
