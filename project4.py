data = []

def input_data():
    """Step 1: Input Data"""
    global data
    arr = input("Enter data for a 1D array (separated by spaces): ")
    data = list(map(int, arr.strip().split()))
    print("\nData has been stored successfully!\n")

def show_data_summary():
    """Step 2: Display Data Summary (built-in functions)"""
    print("\nData Summary:")
    print("- Total elements:", len(data))
    print("- Minimum value:", min(data))
    print("- Maximum value:", max(data))
    print("- Sum of all values:", sum(data))
    print("- Average value:", round(sum(data)/len(data), 2), "\n")

def factorial_recursive(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

def filter_data_by_threshold():
    """Step 4: Filter Data by Threshold (lambda function)"""
    thresh = int(input("Enter a threshold value to filter out data above this value: "))
    filtered = list(filter(lambda x: x >= thresh, data))
    print(f"\nFiltered Data (values >= {thresh}):")
    print(", ".join(str(x) for x in filtered) + "\n")

def sort_data():
    """Step 5: Sort Data"""
    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice: ")
    if choice == '1':
        sorted_data = sorted(data)
        print("\nSorted Data in Ascending Order:")
    else:
        sorted_data = sorted(data, reverse=True)
        print("\nSorted Data in Descending Order:")
    print(", ".join(str(x) for x in sorted_data) + "\n")

def dataset_statistics(arr):
    """Returns multiple statistics on the array"""
    minimum = min(arr)
    maximum = max(arr)
    summation = sum(arr)
    average = round(summation / len(arr), 2)
    return minimum, maximum, summation, average

def show_dataset_statistics():
    """Step 6: Display Dataset Statistics (multiple return values)"""
    min_val, max_val, total, avg = dataset_statistics(data)
    print("\nDataset Statistics:")
    print(f"- Minimum value: {min_val}")
    print(f"- Maximum value: {max_val}")
    print(f"- Sum of all values: {total}")
    print(f"- Average value: {avg}\n")

def main_menu():
    print("Welcome to the Data Analyzer and Transformer Program")
    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")
        choice = input("Please enter your choice: ").strip()

        if choice == '1':
            input_data()
        elif choice == '2':
            show_data_summary()
        elif choice == '3':
            n = int(input("Enter a number to calculate its factorial: "))
            print(f"\nFactorial of {n} is: {factorial_recursive(n)}\n")
        elif choice == '4':
            filter_data_by_threshold()
        elif choice == '5':
            sort_data()
        elif choice == '6':
            show_dataset_statistics()
        elif choice == '7':
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()

print("Thank you for visiting")