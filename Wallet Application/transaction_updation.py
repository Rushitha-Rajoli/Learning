from login_register import login, register_user, load_users, save_users
from datetime import datetime

# Check balance function
def check_balance(user):
    print(f"Your current balance is: ${user['balance']}")

# Add funds function
def add_funds(user, users):
    amount = float(input("Enter amount to deposit: "))
    if amount > 1:
        user["balance"] += amount
        user["transaction_history"].append({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Dynamic Date
            "Type": "Deposit",
            "Amount": f"+${amount}",
            "Balance": f"${user['balance']}"
        })

        # Update user data in users list
        for u in users:
            if u["username"] == user["username"]:
                u.update(user)
        save_users(users)  # Save the updated balance
        print(f"Funds added! New Balance: ${user['balance']}")

    else:
        print("Error: Enter a valid amount!")

# Make a payment function
def make_payment(user, users):
    amount = float(input("Enter amount to pay: "))
    if amount > 0 and user["balance"] >= amount:
        user["balance"] -= amount
        user["transaction_history"].append({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Dynamic Date
            "Type": "Payment",
            "Amount": f"-${amount}",
            "Balance": f"${user['balance']}"
        })
        # Update user data in users list
        for u in users:
            if u["username"] == user["username"]:
                u.update(user)

        save_users(users)  #Save changes
        print(f"Payment Successful! New Balance: ${user['balance']}")
    elif amount <= 0:
        print("Error: Enter a valid amount!")
    else:
        print("Error: Insufficient balance!")

# Apply coupon function
def apply_coupon(user, users):
    coupon_code = input("Enter coupon code: ").strip()
    if coupon_code == "SAVE10" and user['balance'] >=0:
        bonus = user["balance"] * 0.10
        user["balance"] += bonus
        user["transaction_history"].append({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Dynamic Date
            "Type": "Coupon",
            "Amount": f"+${bonus}",
            "Balance": f"${user['balance']}"
        })

        # Update user data in users list
        for u in users:
            if u["username"] == user["username"]:
                u.update(user)

        save_users(users)  # Save changes
        print(f"Coupon Applied! Bonus received. New Balance: ${user['balance']}")
    else:
        print("Invalid coupon code.")

# View transaction history
def view_transactions(user):
    if user["transaction_history"]:
        print("\nTransaction History:")
        print(f"{'Date'} | {'Type'} | {'Amount'} | {'Balance'}")
        print("-" * 50)
        for tx in sorted(user["transaction_history"], key=lambda x: x["Date"]):  #Sorted by date
            print(f"{tx['Date']} | {tx['Type']} | {tx['Amount']} | {tx['Balance']}")
    else:
        print("No transactions yet.")


# Update user profile
def update_profile(user, users):
    email = input("Enter new email: ").strip()
    phone = input("Enter new phone number: ").strip()
    user["email"] = email
    user["phone"] = phone
    save_users(users)# Save profile updates
    print("Profile Updated Successfully!")

def main():
    users = load_users()  #  Load users once at the start
    user = None

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1":
            user = register_user()
            users = load_users()  #  Reload users after registration
        elif option == "2":
            user = login()
            if user:  # Reload users only if login is successful
                users = load_users()
            else:
                continue
        if user:
            while True:
                print("\nWallet Menu:")
                print("4. Check Balance")
                print("5. Add Funds")
                print("6. Make Payment")
                print("7. Apply Coupon")
                print("8. View Transactions")
                print("9. Update Profile")
                print("10. Logout")

                choice = input("Select an option: ")

                if choice == "4":
                    check_balance(user)
                elif choice == "5":
                    add_funds(user, users)
                elif choice == "6":
                    make_payment(user, users)
                elif choice == "7":
                    apply_coupon(user, users)
                elif choice == "8":
                    view_transactions(user)
                elif choice == "9":
                    update_profile(user, users)
                elif choice == "10":
                    print("Logging out...")
                    user = None
                    break
                else:
                    print("Invalid option. Try again.")
        elif option == "3":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
