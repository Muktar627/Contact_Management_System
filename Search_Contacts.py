
def Func_search_contacts(all_contacts):
    if not all_contacts:
        print("\033[31mNo Contact Available in System.\033[0m")
        return all_contacts  # Return unchanged if there are no contact

    # Ask for the phone number to search
    searched_phone_Number = input("Enter Phone Number for Searching: ").strip()

    # Search for the contact by phone number
    contact_found = False
    for contact in all_contacts:
        if contact['Phone'] == searched_phone_Number:
            print("\n\033[32m===Contact Found and Details are below===\033[0m")
            print("-" * 80)
            print(f"\033[34m{'Name':<25} {'Email':<30} {'Phone Number':<15} {'Address':<25}\033[0m")
            print("-" * 80)
            print(f"{contact['Name']:<25} {contact['Email']:<30} {contact['Phone']:<15} {contact['Address']:<25}")
            contact_found = True
            break
    if not contact_found:
        print(f"\033[31mContact with phone number {searched_phone_Number} not found in the System.\033[0m")

    return all_contacts  # Return the updated list of contact