import json
# Load users from the JSON file
def load_users():
   try:
       with open("users.json", "r") as file:
           return json.load(file)  # Returns a list of user dictionaries
   except FileNotFoundError:
       return []

# Save users to the JSON file
def save_users(users):
   with open("users.json", "w") as file:
       json.dump(users, file, indent=4)

# Register new user function
def register_user():
   users = load_users()

   username = input("Enter username: ").strip()
   password = input("Enter password: ").strip()

   for user in users:
       if user["username"] == username:
           print("Username already taken! Choose a different username.")
           return None

   new_user = {
       "username": username,
       "password": password,
       "balance": 0,
       "email": "",
       "phone": "",
       "transaction_history": [],
   }
   users.append(new_user)
   save_users(users)

   print("User Registered Successfully!")
   return new_user  # Return the new user object

# Login function
def login():
   users = load_users()
   username = input("Enter username: ").strip()
   password = input("Enter password: ").strip()

   for user in users:
       if user["username"] == username and user["password"] == password:
           print("Login Successful!")
           return user  # Return the user object

   print("User not found or incorrect password.")
   return None

