from Save_Contact import Func_Save_Contacts

def Func_remove_contacts(all_contacts):
    if not all_contacts:
        print("\033[31mNo Contact to Delete.\033[0m")
        return all_contacts  # Return unchanged if there are no contact

    # Ask for the phone number to remove
    removed_phone_Number = input("Enter Phone Number for Deletion: ").strip()

    # Search for the contact by phone number
    contact_found = False
    for contact in all_contacts:
        if contact['Phone'] == removed_phone_Number:
            all_contacts.remove(contact)  # Remove the contact from the list
            print(f"\033[33mContact with Phone Number {removed_phone_Number } Deleted successfully.\033[0m")
            Func_Save_Contacts(all_contacts) # Save the updated contacts list
            contact_found = True
            break

    if not contact_found:
           print(f"\033[31mContact with phone number {removed_phone_Number } not found in the System.\033[0m")

    return all_contacts  # Return the updated list of contact

