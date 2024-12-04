"""Saves contacts from the system to the CSV file."""
import csv
def Func_Save_Contacts(all_contacts, filename="all_contacts_Book.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            # Define the CSV writer and the fieldnames (headers)
            fieldnames = ['Name', 'Email', 'Phone', 'Address']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Write the header row
            writer.writeheader()
            # Write each contact as a row in the CSV file
            writer.writerows(all_contacts)
            print("\033[32mContact List Updated successfully.\033[0m")

    except Exception as e:
        print(f"\033[31mError saving contacts to CSV: {e}\033[0m")