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
    search_category = input("Enter the category to search in (name, phone, email, tags): ")
    search_term = input("Enter the search term: ")

    for contact in contacts["contacts"]:
        if search_category == "name":
            search_pattern = re.compile(search_term, re.IGNORECASE)
            if search_pattern.search(contact["name"]):
                option = input("Merge(m) or remove (r)? ")
                if option.lower() == "r":
                    contacts["contacts"].remove(contact)
                elif option.lower() == "m":
                    phone = input("Enter the new phone number (leave blank to keep it unchanged): ")
                    email = input("Enter the new email address (leave blank to keep it unchanged): ")
                    tags = input("Enter the new tags (comma-separated, leave blank to keep them unchanged): ")

                    if phone:
                        contact["phone"] = phone
                    if email:
                        contact["email"] = email
                    if tags:
                        new_tags = tags.split(',')
                        contact["tags"].extend(new_tags)

                    print("Contact updated successfully.")
                    return contact

        elif search_category == "phone":
            search_pattern = re.compile(search_term, re.IGNORECASE)
            if search_pattern.search(contact["phone"]):
                option = input("Merge(m) or remove (r)? ")
                if option.lower() == "r":
                    contacts["contacts"].remove(contact)
                elif option.lower() == "m":
                    name = input("Enter the new name (leave blank to keep it unchanged): ")
                    email = input("Enter the new email address (leave blank to keep it unchanged): ")
                    tags = input("Enter the new tags (comma-separated, leave blank to keep them unchanged): ")

                    if name:
                        contact["name"] = name
                    if email:
                        contact["email"] = email
                    if tags:
                        new_tags = tags.split(',')
                        contact["tags"].extend(new_tags)

                    print("Contact updated successfully.")
                    return contact

        elif search_category == "email":
            search_pattern = re.compile(search_term, re.IGNORECASE)
            if search_pattern.search(contact["email"]):
                option = input("Merge(m) or remove (r)? ")
                if option.lower() == "r":
                    contacts["contacts"].remove(contact)
                elif option.lower() == "m":
                    name = input("Enter the new name (leave blank to keep it unchanged): ")
                    phone = input("Enter the new phone number (leave blank to keep it unchanged): ")
                    tags = input("Enter the new tags (comma-separated, leave blank to keep them unchanged): ")

                    if name:
                        contact["name"] = name
                    if phone:
                        contact["phone"] = phone
                    if tags:
                        new_tags = tags.split(',')
                        contact["tags"].extend(new_tags)

                    print("Contact updated successfully.")
                    return contact

        elif search_category == "tags":
            search_pattern = re.compile(search_term, re.IGNORECASE)
            if any(search_pattern.search(tag) for tag in contact["tags"]):
                option = input("Merge(m) or remove (r)? ")
                if option.lower() == "r":
                    contacts["contacts"].remove(contact)
                elif option.lower() == "m":
                    name = input("Enter the new name (leave blank to keep it unchanged): ")
                    phone = input("Enter the new phone number (leave blank to keep it unchanged): ")
                    email = input("Enter the new email address (leave blank to keep it unchanged): ")

                    if name:
                        contact["name"] = name
                    if phone:
                        contact["phone"] = phone
                    if email:
                        contact["email"] = email

                    print("Contact updated successfully.")
                    return contact

    print("Contact not found.")
    return None
                
def filter_contacts_by_tag(contacts, tag):
    filtered_contacts = []

    for contact in contacts["contacts"]:
        tags_match = any(re.search(fr"\b{re.escape(tag)}\b", t, flags=re.IGNORECASE) for t in contact.get("tags", []))

        if tags_match:
            filtered_contacts.append(contact)

    print("Filter results: \n")
    for contact in filtered_contacts:
        print_single_contact(contact)

def fuzzy_search(contacts, search_term):
    search_results = []

    for contact in contacts["contacts"]:
        name_match = re.match(fr".*{re.escape(search_term)}.*", contact.get("name", ""), flags=re.IGNORECASE)
        phone_match = re.match(fr".*{re.escape(search_term)}.*", contact.get("phone", ""), flags=re.IGNORECASE)
        email_match = re.match(fr".*{re.escape(search_term)}.*", contact.get("email", ""), flags=re.IGNORECASE)
        tags_match = re.findall(fr"\b{re.escape(search_term)}\b", ', '.join(contact.get("tags", [])), flags=re.IGNORECASE)

        if name_match or phone_match or email_match or tags_match:
            search_results.append(contact)

    return search_results

def print_single_contact(contact):
    print("Name:", contact["name"])
    print("Phone:", contact["phone"])
    print("Email:", contact["email"])
    print("Tags:", ', '.join(contact["tags"]))
    print()

def print_contacts(contacts):
    for contact in contacts["contacts"]:
        print_single_contact(contact)

if __name__ == "__main__":
    file_path = "contacts.json"
    contacts = load_contacts(file_path)

    quit = False
    #print_contacts(contacts)
    while quit == False:
        choice = input("Choose the mode you want (view by tags/add/update/search/quit): ")

        if choice.lower() == "view by tags":
            contacts = load_contacts(file_path)
            tag = input("Input tag: ")
            filter_contacts_by_tag(contacts, tag)
        elif choice.lower() == "add":
            add_contact(contacts)
            save_contacts(file_path, contacts)
        elif choice.lower() == "update":
            update_contact(contacts)
            save_contacts(file_path, contacts)
            contacts = load_contacts(file_path)
            updated_contact = update_contact(contacts)
            if updated_contact:
                print("Updated Contact:")
                print_single_contact(updated_contact)
        elif choice.lower() == "search":
            sterm = input("Input search term: ")
            search_results = fuzzy_search(contacts, sterm)
            print("Search results: \n")
            for result in search_results:
                print_single_contact(result)
        elif choice.lower() == "quit":
            quit = True
        else:
            print("Invalid choice.")

    save_contacts(file_path, contacts)

