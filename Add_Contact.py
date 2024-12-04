from Save_Contact import Func_Save_Contacts
from Prevent_Duplicate_Numbers import Func_Duplicate_Checking

def Func_add_contact(all_contacts):
    try:
        # Ensure phone number is valid and unique
        phone=Func_Duplicate_Checking(all_contacts)
        # Input and validate the name (ensuring it is a valid string)
        while True:
            name=input("Enter Name: ").strip()
            if not name.isalpha():  # Check if the name contains only alphabetic characters
                print("\033[31mError: Name must contain only alphabetic characters.\033[0m")
            
            else:
                break
        email=input("Enter Email: ").strip()        
        #phone=int(input("Enter Phone Number: "))
        address=input("Enter Address: ").strip()

        # Validate inputs before creating the contact
        if not name or not email or not address:
            print("\033[31mError: Name, Email, or Address cannot be empty.\033[0m")
            return all_contacts
        
        # Create a new contact dictionary
        New_contact={
            "Name":name,
            "Email":email,
            "Phone":phone,
            "Address":address
            }
        all_contacts.append(New_contact)
        Func_Save_Contacts(all_contacts)
        print(f"\033[32mConact Added Successfully\033[0m")
        return all_contacts
    except Exception as e:
        print(f"\033[31mError adding contact: {e}\033[0m")