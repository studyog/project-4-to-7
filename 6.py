import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        entry = input("Enter your journal entry:\n")
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        try:
            with open(self.filename, 'a') as file:
                file.write(f"{timestamp}\n{entry}\n\n")
            print("Entry added successfully!")
        except Exception as e:
            print(f"Error: Could not add entry. {e}")

    def view_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries found. Start by adding a new entry!")
            return
        print("Your Journal Entries:")
        print("-" * 40)
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                print(content if content.strip() else "No entries to show.")
        except Exception as e:
            print(f"Error: {e}")

    def search_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries found. Start by adding a new entry!")
            return
        keyword = input("Enter a keyword or date to search: ").strip()
        found = False
        print("Matching Entries:")
        print("-" * 40)
        try:
            with open(self.filename, 'r') as file:
                entries = file.read().split('\n\n')
                for entry in entries:
                    if keyword.lower() in entry.lower():
                        print(entry)
                        print()
                        found = True
            if not found:
                print(f"No entries were found for the keyword: {keyword}.")
        except Exception as e:
            print(f"Error: {e}")

    def delete_all_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return
        confirm = input("Are you sure you want to delete all entries? (yes/no): ").strip().lower()
        if confirm == 'yes':
            try:
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            except Exception as e:
                print(f"Error: Could not delete entries. {e}")
        else:
            print("Deletion cancelled.")

def main():
    jm = JournalManager()
    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Invalid option. Please select a valid option from the menu.")
            continue

        if choice == 1:
            jm.add_entry()
        elif choice == 2:
            jm.view_entries()
        elif choice == 3:
            jm.search_entries()
        elif choice == 4:
            jm.delete_all_entries()
        elif choice == 5:
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option from the menu.")

if __name__ == '__main__':
    main()  