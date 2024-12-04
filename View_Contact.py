
def Func_view_all_contact(all_contacts):
    # If there are no contacts in the system
    if not all_contacts:
        print("\n\033[31mNo contacts found in the Contact Management System.\033[0m")
        return all_contacts
    
    # If contact available then Display contacts in a table format
    print("\n\033[32m=== Contact List ===\033[0m")
    print("-" * 80)
    # Print the header
    print(f"\033[34m{'Name':<25} {'Email':<30} {'Phone Number':<15} {'Address':<25}\033[0m")
    print("-" * 80)
    for contact in all_contacts:
        #print(f"Name: {contact['Name']:<25} |Email: {contact['Email']:<30}| Phone Number: {contact['Phone']:<15} | Address: {contact['Address']}")
        print(f"{contact['Name']:<25} {contact['Email']:<30} {contact['Phone']:<15} {contact['Address']:<25}")
    print("-" * 80)
    return all_contacts