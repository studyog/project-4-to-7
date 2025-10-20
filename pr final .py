import datetime
import random
import os

class ATMUser:
    def __init__(self, account_no, name, balance, pin):
        self.account_no = account_no
        self.name = name
        self.balance = balance
        self.pin = pin
        self.transactions = []

    def __str__(self):
        return f"Account: {self.account_no} | Name: {self.name} | Balance: {self.balance} | PIN: {self.pin}"

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        txn_id = self._generate_txn_id()
        txn_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"Deposit ₹{amount} on {txn_time} (TXN: {txn_id})")
        print(f"Deposit successful.\nNew Balance: ₹{self.balance:.2f}\nTransaction ID: {txn_id} | Date: {txn_time}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
            return
        self.balance -= amount
        txn_id = self._generate_txn_id()
        txn_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"Withdraw ₹{amount} on {txn_time} (TXN: {txn_id})")
        print(f"Withdraw successful.\nRemaining Balance: ₹{self.balance:.2f}\nTransaction ID: {txn_id} | Date: {txn_time}")

    def show_transactions(self):
        print("--- Last 5 Transactions ---")
        for idx, txn in enumerate(self.transactions[-5:], 1):
            print(f"[{idx}] {txn}")

    def update_pin(self, new_pin):
        self.pin = new_pin
        print("PIN updated successfully!")

    def _generate_txn_id(self):
        return ''.join(random.choices('0123456789abcdef', k=8))

    def __del__(self):
        pass

def save_users(users):
    with open("users.txt", "w") as f:
        for u in users.values():
            f.write(f"{u.account_no}|{u.name}|{u.balance}|{u.pin}\n")

def save_transactions(users):
    with open("transactions.txt", "w") as f:
        for u in users.values():
            for txn in u.transactions:
                f.write(f"{txn} | Account: {u.account_no}\n")

def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                try:
                    acc, name, bal, pin = line.strip().split("|")
                    users[int(acc)] = ATMUser(int(acc), name, float(bal), int(pin))
                except Exception as e:
                    continue
    return users

def load_transactions(users):
    if os.path.exists("transactions.txt"):
        with open("transactions.txt", "r") as f:
            for line in f:
                parts = line.strip().split(" | Account: ")
                if len(parts) == 2:
                    txn, acc = parts
                    acc = int(acc)
                    if acc in users:
                        users[acc].transactions.append(txn)

def generate_account_no(users):
    return max(users.keys(), default=1000) + 1

def generate_pin():
    return random.randint(1000, 9999)

def main():
    users = load_users()
    load_transactions(users)

    while True:
        print("\nWelcome to the SMART ATM SYSTEM")
        print("1. Create New Account")
        print("2. Login to Existing Account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            try:
                initial_deposit = float(input("Initial deposit amount: "))
                account_no = generate_account_no(users)
                pin = generate_pin()
                user = ATMUser(account_no, name, initial_deposit, pin)
                users[account_no] = user
                print(f"Your account number is: {account_no}")
                print(f"Your temporary PIN is: {pin}")
                print("Account successfully created!")
            except Exception as e:
                print("Invalid input! Please try again.")

        elif choice == "2":
            try:
                acc = int(input("Enter Account Number: "))
                pin = int(input("Enter PIN: "))
                user = users.get(acc)
                if user and user.pin == pin:
                    print(f"Login successful! Welcome, {user.name}")
                    while True:
                        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. View Last 5 Transactions\n5. Change PIN\n6. Logout")
                        sub_choice = input("Enter your choice: ")
                        if sub_choice == "1":
                            user.check_balance()
                        elif sub_choice == "2":
                            try:
                                amt = float(input("Enter deposit amount: "))
                                user.deposit(amt)
                            except:
                                print("Invalid deposit amount.")
                        elif sub_choice == "3":
                            try:
                                amt = float(input("Enter withdrawal amount: "))
                                user.withdraw(amt)
                            except:
                                print("Invalid withdrawal amount.")
                        elif sub_choice == "4":
                            user.show_transactions()
                        elif sub_choice == "5":
                            try:
                                curr_pin = int(input("Enter your current PIN: "))
                                if curr_pin == user.pin:
                                    new_pin = int(input("Enter new PIN: "))
                                    user.update_pin(new_pin)
                                else:
                                    print("Incorrect current PIN!")
                            except:
                                print("Invalid PIN entered.")
                        elif sub_choice == "6":
                            print(f"Logging out... Thank you, {user.name}!")
                            break
                        else:
                            print("Invalid choice.")
                else:
                    print("Account number or PIN is incorrect!")
            except:
                print("Error: Invalid login details.")

        elif choice == "3":
            print("Exiting... All data has been saved.")
            save_users(users)
            save_transactions(users)
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()