import csv
import os

def Func_load_contacts(filename="all_contacts_Book.csv"):
    """Load all contacts from a CSV file."""
    contacts = []
    
    if os.path.exists(filename):
        try:
            with open(filename, mode="r", newline='') as file:
                reader = csv.DictReader(file)
                # Read each row as a dictionary and append it to the contacts list
                for row in reader:
                    contacts.append(row)
            print("\033[32mContacts loaded successfully.\033[0m")
        except Exception as e:
            print(f"\033[31mError loading contacts: {e}\033[0m")
    
    else:
        print("\033[33mNo saved contacts found. Starting with an empty contact list.\033[0m")
    
    return contacts