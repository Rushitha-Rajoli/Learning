import json  # Import the JSON module

# Initialize an empty list to store user dictionaries
users = []

# Number of users
num_users = int(input("Enter the number of users: "))

# Loop through and collect data for each user
for i in range(num_users):
    print("Enter details for User ",(i + 1))

    # Take input from the user
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")

    # Create a dictionary for each user
    user_data = {
        "name": name,
        "age": age,
        "employee_id": employee_id
    }
    users.append(user_data)# Append to the users list

# **Convert Python object (list of dictionaries) to JSON**
json_data = json.dumps(users,indent=2)  # Convert list of dicts to JSON format with indentation
print("JSON Data:")
print(json_data)

# Convert JSON back to Python object**
python_obj = json.loads(json_data)  # Convert JSON string back to Python object (list of dicts)
print("Converted Back to Python Object:")
print(python_obj)
