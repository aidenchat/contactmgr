import json
import re

file_path = "contacts.json"
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

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")

    for contact in contacts["contacts"]:
        if contact["name"].lower() == name.lower():
            phone = input("Enter the new phone number (leave blank to keep it unchanged): ")
            email = input("Enter the new email address (leave blank to keep it unchanged): ")
            tags = input("Enter the new tags (comma-separated, leave blank to keep them unchanged): ")

            if phone:
                contact["phone"] = phone
            if email:
                contact["email"] = email
            if tags:
                contact["tags"] = tags.split(',')

            print("Contact updated successfully.")
            return

    print("Contact not found.")

def filter_contacts_by_tag(contacts, tag):
    filtered_contacts = []
    for contact in contacts["contacts"]:
        if tag in contact["tags"]:
            filtered_contacts.append(contact)
    return filtered_contacts

def search_contacts_by_name(contacts, name):
    search_results = []
    pattern = f".*{re.escape(name)}.*" # Create a pattern
    for contact in contacts["contacts"]:
        contact_name = contact["name"]
        if re.match(pattern, contact_name, flags=re.IGNORECASE):
            search_results.append(contact)
        return search_results
    # for contact in contacts["contacts"]:
    #     if name.lower() in contact["name"].lower():
    #         search_results.append(contact)
    # return search_results

def print_dict(dict):
    for contact in dict:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Tags:", ', '.join(contact["tags"]))
        print()


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
  
    quit = False
    while quit == False:
        choice = input("Do you want to add a new contact (add), update an existing contact (update) or quit the contact (quit)? ")

        if choice.lower() == "add":
            add_contact(contacts)
        elif choice.lower() == "update":
            update_contact(contacts)
        elif choice.lower() == "quit":
            quit = True
        else:
            print("Invalid choice.")

    save_contacts(file_path, contacts)
        
