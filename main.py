import json

def load_contacts(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_contacts(file_path, contacts):
    with open(file_path, 'w') as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    tags = input("Enter tags (comma-separated): ").split(',')

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "tags": tags
    }

    contacts["contacts"].append(new_contact)
    print("Contact added successfully.")

# Main program

if __name__ == "__main__":
    file_path = "contacts.json"
    contacts = load_contacts(file_path)

    print("Existing Contacts:")
    for contact in contacts["contacts"]:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Tags:", ', '.join(contact["tags"]))
        print()

    add_contact(contacts)

    save_contacts(file_path, contacts)