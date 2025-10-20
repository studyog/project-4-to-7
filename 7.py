import math
import random
import uuid
import datetime

def show_current_date_time():
    now = datetime.datetime.now()
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def date_difference():
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")
    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    diff = abs((d2 - d1).days)
    print("Difference: {} days".format(diff))

def factorial_calc():
    num = int(input("Enter a number: "))
    print("Factorial: {}".format(math.factorial(num)))

def compound_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest (in %): "))
    t = int(input("Enter time (in years): "))
    ci = p * ((1 + r/100) ** t)
    print("Compound Interest: {:.2f}".format(ci))

def random_number():
    print("Random Number:", random.randint(1, 1000))

def random_list():
    size = int(input("Enter list size: "))
    lst = [random.randint(1, 100) for _ in range(size)]
    print("Random List:", lst)

def random_password():
    length = int(input("Enter password length: "))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    pwd = ''.join(random.choice(chars) for _ in range(length))
    print("Generated Password:", pwd)

def random_otp():
    otp = random.randint(100000, 999999)
    print("Generated OTP:", otp)

def uuid_gen():
    print("Generated UUID:", str(uuid.uuid4()))

def create_file():
    fname = input("Enter file name: ")
    with open(fname, "w") as f:
        print("File created successfully!")

def write_file():
    fname = input("Enter file name: ")
    data = input("Enter data to write: ")
    with open(fname, "w") as f:
        f.write(data)
    print("Data written successfully!")

def read_file():
    fname = input("Enter file name: ")
    with open(fname, "r") as f:
        print("File Content:\n" + f.read())

def append_file():
    fname = input("Enter file name: ")
    data = input("Enter data to append: ")
    with open(fname, "a") as f:
        f.write(data)
    print("Data appended successfully!")

def explore_module():
    mod_name = input("Enter module name to explore: ")
    if mod_name == "math":
        print("Available Attributes in math module:")
        print(dir(math))

def main():
    while True:
        print("\n--- Welcome to Multi-Utility Toolkit ---")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("1. Show Current Date and Time")
            print("2. Calculate Difference Between Dates")
            sub = input("Enter your choice: ")
            if sub == "1":
                show_current_date_time()
            elif sub == "2":
                date_difference()

        elif choice == "2":
            print("1. Calculate Factorial")
            print("2. Calculate Compound Interest")
            sub = input("Enter your choice: ")
            if sub == "1":
                factorial_calc()
            elif sub == "2":
                compound_interest()

        elif choice == "3":
            print("1. Generate Random Number")
            print("2. Generate Random List")
            print("3. Generate Random Password")
            print("4. Generate Random OTP")
            sub = input("Enter your choice: ")
            if sub == "1":
                random_number()
            elif sub == "2":
                random_list()
            elif sub == "3":
                random_password()
            elif sub == "4":
                random_otp()

        elif choice == "4":
            uuid_gen()

        elif choice == "5":
            print("1. Create New File")
            print("2. Write to File")
            print("3. Read from File")
            print("4. Append to File")
            sub = input("Enter your choice: ")
            if sub == "1":
                create_file()
            elif sub == "2":
                write_file()
            elif sub == "3":
                read_file()
            elif sub == "4":
                append_file()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()