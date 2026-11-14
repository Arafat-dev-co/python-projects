import json

filename ='contact.json'

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    def __str__(self):
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.json"

    def load_contacts(self):
        try:
            with open(self.filename) as file_object:
                contents = json.load(file_object)

            
            for item in contents:
                new_contact = Contact(item["name"], item["phone"], item["email"])
                self.contacts.append(new_contact)    

        except FileNotFoundError:
            pass


    def save_contacts(self):
        data_to_save = []

        for data in self.contacts:
            data_to_save.append(data.to_dict())

        with open(self.filename, 'w') as file_object:
            json.dump(data_to_save, file_object, indent=4) 

    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def get_all_contacts(self):
        return self.contacts

    def search_contact(self, search_name):
        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                return contact
        return None


    def update_contact(self, name, new_phone, new_email):
        update = self.search_contact(name)
        if update is not None:
            update.phone = new_phone
            update.email = new_email
            return True
        else:
            return False


    def delete_contact(self, name):
        for user in self.contacts:
            if user.name.lower() == name.lower():
                self.contacts.remove(user)
                return True  
        return False

def main():
    manager = ContactManager()
    manager.load_contacts()

    while True:
        print("\n--- CONTACT MANAGER ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            name = input("Enter your name: ")

            if name == '':
                print("Pls enter a name\n")
                continue

            phone = input("Enter your phone number: ")

            if not phone.isdigit():
                print("Must be number only\n")
                continue

            email = input("Enter your email: ")
            if '@' not in email or "." not in email.split("@")[-1]:
                print("Invalid email\n")
                continue

            user0 = Contact(name, phone, email)

            result1 = manager.add_contact(user0)
            result2 = manager.save_contacts()
            print("Contact Added Successfully")

        elif choice == "2":
            result3 = manager.get_all_contacts()
            if len(result3) == 0:
                print("The list is empty")

            else:
                for result in result3:
                    print(result)

        elif choice == "3":
            name1 = input("Enter your name: ")

            result4 = manager.search_contact(name1)
            if result4 is not None:
                print(result4)
            else:
                print("Not found")


        elif choice == "4":
            name = input("Enter your name: ")
            if name == '':
                print("Pls enter a name\n")
                continue

            new_phone = input("Enter your phone number: ")
            if not new_phone.isdigit():
                print("Must be number only\n")
                continue
            
            new_email = input("Enter your email: ")
            if '@' not in new_email or "." not in new_email.split("@")[-1]:
                print("Invalid email\n")
                continue


            result5 = manager.update_contact(name, new_phone, new_email)
            if result5:
                save = manager.save_contacts()
                print("Sucessfully Update and Saved")
            else:
                print("Contact not found")

        elif choice == "5":
            name = input("Enter your name: ")
            result6 = manager.delete_contact(name)
        

            if result6:
                save = manager.save_contacts()
                print("Sucessfully Deleted")
            else:
                print("Contact not found")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
