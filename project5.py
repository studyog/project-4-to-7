
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id      
        self.__salary = salary      
    
    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary
   
    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        super().display()
        print(f"Employee ID: {self.__emp_id}")
        print(f"Salary: ${self.__salary:.1f}")

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

def main():
    print("--- Python OOP Project: Employee Management System ---\n")

    person = None
    employee = None
    manager = None

    while True:
        print("Choose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            person = Person(name, age)
            print(f"\nPerson created with name: {name} and age: {age}.\n")

        elif choice == '2':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            employee = Employee(name, age, emp_id, salary)
            print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary:.1f}.\n")

        elif choice == '3':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            manager = Manager(name, age, emp_id, salary, dept)
            print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary:.1f}, and department: {dept}.\n")

        elif choice == '4':
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            show = input("Enter your choice: ")

            if show == '1' and person:
                print("\nPerson Details:")
                person.display()
            elif show == '2' and employee:
                print("\nEmployee Details:")
                employee.display()
            elif show == '3' and manager:
                print("\nManager Details:")
                manager.display()
            else:
                print("\nNo details found for that choice.\n")

        elif choice == '5':
            print("\nExiting the system. All resources have been freed.\n")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
