from built import login, register_user, load_users, save_users

# Check balance function
def check_balance(user):
   print(f"Your current balance is: ${user['balance']}")


# Add funds function
def add_funds(user):
   amount = float(input("Enter amount to deposit: "))
   user["balance"] += amount
   user["transaction_history"].append(f"Deposited ${amount}")
   save_users(load_users())
   print(f"New Balance: ${user['balance']}")


# Make a payment function
def make_payment(user):
   amount = float(input("Enter amount to pay: "))
   if user["balance"] >= amount:
       user["balance"] -= amount
       user["transaction_history"].append(f"Paid ${amount}")
       save_users(load_users())
       print(f"Payment Successful! New Balance: ${user['balance']}")
   else:
       print("Error: Insufficient balance!")


# Apply coupon function
def apply_coupon(user):
   coupon_code = input("Enter coupon code: ").strip()


   if coupon_code == "SAVE10":
       bonus = user["balance"] * 0.10
       user["balance"] += bonus
       user["transaction_history"].append(f"Coupon Applied: +${bonus}")
       save_users(load_users())
       print(f"Coupon Applied! Bonus received. New Balance: ${user['balance']}")
   else:
       print("Invalid coupon code.")


# View transaction history
def view_transactions(user):
   if user["transaction_history"]:
       print("Transaction History:")
       for transaction in user["transaction_history"]:
           print(transaction)
   else:
       print("No transactions yet.")


# Update user profile
def update_profile(user):
   email = input("Enter new email: ").strip()
   phone = input("Enter new phone number: ").strip()

   user["email"] = email
   user["phone"] = phone
   save_users(load_users())

   print("Profile Updated Successfully!")

# Main function to run the wallet system
def main():
   user = None
   while True:
       print("\n1. Register")
       print("2. Login")
       print("3. Exit")

       option = input("Choose an option: ")

       if option == "1":
           user = register_user()
       elif option == "2":
           user = login()


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
                   add_funds(user)
               elif choice == "6":
                   make_payment(user)
               elif choice == "7":
                   apply_coupon(user)
               elif choice == "8":
                   view_transactions(user)
               elif choice == "9":
                   update_profile(user)
               elif choice == "10":
                   print("Logging out...")
                   user = None
                   break
               else:
                   print("Invalid option. Try again.")
       elif option == "3":
           print("Thankyou for Visting!")
           break
       else:
           print("Invalid option. Try again.")


if __name__ == "__main__":
   main()
