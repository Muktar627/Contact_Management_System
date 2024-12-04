
def Func_Duplicate_Checking(all_contacts):
    while True:
        phone_Number=input("Enter Phone Number: ").strip()
        # Validate that the phone number contains only digits
        if not phone_Number.isdigit():
            print("\033[31mError: Phone number must contain only digits.\033[0m")
            continue  # Prompt for phone number again
        for contact in all_contacts:
            if contact['Phone'] == phone_Number:
                print(f"\033[31mProvided Number {phone_Number} Already Exist.\033[0m")
                break
        else:
            print(f"\033[32mProvided Number {phone_Number} is Unique.\033[0m")
            return phone_Number
