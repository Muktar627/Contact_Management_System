"""
# Text Colors
print("\033[31mThis is red text\033[0m")  # Red text
print("\033[32mThis is green text\033[0m")  # Green text
print("\033[33mThis is yellow text\033[0m")  # Yellow text
print("\033[34mThis is blue text\033[0m")  # Blue text

# Background Colors
print("\033[41mThis is text with a red background\033[0m")  # Red background
print("\033[42mThis is text with a green background\033[0m")  # Green background

# Bold Text2
print("\033[1mThis is bold text\033[0m")

# Underline Text
print("\033[4mThis is underlined text\033[0m")
"""

import Add_Contact
import View_Contact
from Load_Contact import Func_load_contacts
import Remove_Contact
import Search_Contacts

all_contacts = Func_load_contacts()
#all_contacts = []
while True:
    print("\nWelcome to Contact Management System")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View All Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
  
    user_choice = input("Select Your Choice: ")

    if user_choice == "0":
        print("\n\033[34mThanks for using the Contact Management System.\033[0m\n")
        break
    elif user_choice == "1":
        all_contacts = Add_Contact.Func_add_contact(all_contacts)
    elif user_choice == "2":
        all_contacts = View_Contact.Func_view_all_contact(all_contacts)
    elif user_choice == "3":
        all_contacts = Remove_Contact.Func_remove_contacts(all_contacts)
    elif user_choice == "4":
        all_contacts = Search_Contacts.Func_search_contacts(all_contacts)
    else:
        print("\n\033[31mInvalid choice. Please select a valid option.\033[0m\n")
