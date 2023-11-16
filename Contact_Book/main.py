class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        """
        Add a new contact to the contact book.
        """
        contact = {'Name': name, 'Phone': phone, 'Email': email}
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!\n")

    def view_contacts(self):
        """
        View all contacts in the contact book.
        """
        if not self.contacts:
            print("Contact book is empty.\n")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
            print()

    def search_contacts(self, keyword):
        """
        Search for contacts based on a keyword.
        """
        matching_contacts = [contact for contact in self.contacts
                             if keyword.lower() in contact['Name'].lower() or
                             keyword.lower() in contact['Phone'] or
                             keyword.lower() in contact['Email'].lower()]

        if not matching_contacts:
            print(f"No contacts found with '{keyword}'.\n")
        else:
            print("Matching Contacts:")
            for contact in matching_contacts:
                print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
            print()

def get_user_input(prompt):
    """
    Get user input and handle potential errors.
    """
    while True:
        try:
            user_input = input(prompt)
            return user_input
        except KeyboardInterrupt:
            print("\nOperation canceled by user.")
            exit()

def main():
    contact_book = ContactBook()

    print("Welcome! I am your virtual contacts manager. I can store your contacts for you.")


    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Exit")

        choice = get_user_input("Enter your choice (1-4): ")

        if choice == '1':
            name = get_user_input("Enter contact name: ")
            phone = get_user_input("Enter contact phone number: ")
            email = get_user_input("Enter contact email address: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            keyword = get_user_input("Enter a keyword to search contacts: ")
            contact_book.search_contacts(keyword)
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()

