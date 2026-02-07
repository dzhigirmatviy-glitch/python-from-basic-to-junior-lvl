import json
class Contacts:
    def __init__(self, name, phone, email, number):
        self.name = name
        self.phone = phone
        self.email = email
        self.number = number

    def show(self):
        print(f"{self.number}. {self.name} - {self.phone} - {self.email}")

def collect_contacts_data(loaded_data):
    data = []
    while True:
        try:
            numbers = int(input("input how much contacts would you like to add: "))
            if numbers <= 0:
                print("You must add at least one contact!")
                continue
            for i in range(numbers):
                print(f"\nAdding contact number {i+1}...")
                name = input("input your contact name: ")
                phone = input("input your contact phone: ")
                email = input("input your contact email: ")
                print("✅Contact added!")
                number = len(loaded_data) + i + 1
                new_contact = Contacts(name, phone, email, number)
                data.append(new_contact)
            break
        except ValueError:
            print("Please enter a valid number")
    return data

def show_contacts(all_data):
    print("=== CONTACTS ===")
    for new_contact in all_data:
        new_contact.show()

def find_by_name(all_data):
    contact_name = input("input your contact name to find: ")
    found = False
    for new_contact in all_data:
        if new_contact.name == contact_name:
            new_contact.show()
            found = True
    if not found:
        print("Contact not found!")

def save_data(all_data):
    list_contacts = []
    try:
        for new_contact in all_data:
            list_contacts.append({"name": new_contact.name,
                         "phone": new_contact.phone,
                         "email": new_contact.email,
                         "number": new_contact.number
                         })
        with open("contacts.json", "w", encoding="utf-8") as f:
            json.dump(list_contacts, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        return []

def load_data():
    contact_objects = []
    try:
        with open("contacts.json", "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
        for item in loaded_data:
            contact = Contacts(item["name"], item["phone"], item["email"], item["number"])
            contact_objects.append(contact)
        return contact_objects
    except FileNotFoundError:
        return []

def main():
    loaded_data = load_data()
    while True:
        try:
            print("\n=== CONTACT LIST ===")
            print("1. Add contact")
            print("2. Show all contacts")
            print("3. Find contact by name")
            print("4. Exit")

            choice = int(input("Enter your choice[1-4]: "))
            if choice == 1:
                all_data = collect_contacts_data(loaded_data)
                loaded_data.extend(all_data)
                save_data(loaded_data)
            elif choice == 2:
                show_contacts(loaded_data)
            elif choice == 3:
                find_by_name(loaded_data)
            elif choice == 4:
                print("Goodbye!")
                break
        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()