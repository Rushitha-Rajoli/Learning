import json


# Load users from the JSON file
def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)  # Returns a list of user dictionaries
    except FileNotFoundError:
        print("No user data file found. Starting fresh.")
        return []


# Register new user function
def register_user():
    users = load_users()

    print("Enter username: ")
    username = input().strip()  # Remove any spaces around the username
    print("Enter password: ")
    password = input().strip()  # Remove any spaces around the password

    # Check if user already exists
    for user in users:
        if user['username'] == username:
            print("Username already taken! Please choose a different username.")
            return

    # If username is unique, add the new user
    new_user = {
        "username": username,
        "password": password,
        "balance": 0  # You can add more details if needed
    }
    users.append(new_user)

    # Save the updated user list to the file
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

    print("User Registered Successfully!")


# Login function
def login():
    users = load_users()

    print("Enter username: ")
    username = input().strip()  # Remove any spaces around the username
    print("Enter password: ")
    password = input().strip()  # Remove any spaces around the password

    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Login Successful!")
            return True
    print("User not found or incorrect password.")
    return False


# Main function to drive the menu
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1":
            register_user()
        elif option == "2":
            if login():
                print("Welcome to your wallet!")
                # Further actions after login can be added here.
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
