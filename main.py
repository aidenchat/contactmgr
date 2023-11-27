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

def update_contact(contacts): #should can search by any category?
    name = input("Enter the name of the contact to update: ")

    for contact in contacts["contacts"]:
        name_pattern = re.compile(name, re.IGNORECASE)

        if name_pattern.search(contact["name"]) :
            option= input("Merge(m) or remove (r)? ") #both merge and r still sucks: can't merge phone no, can't remove
            if option.lower()== "r":
                    if contact["name"].lower() == name.lower():
                        del contacts["contacts"]
            elif option.lower()== "m":
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
                
def filter_contacts_by_tag(contacts, tag): #not yet work
    filtered_contacts = []
    for contact in contacts["contacts"]:
        if tag.lower() in contact["tags"]: 
            filtered_contacts.append(contact)
    return filtered_contacts

def fuzzy_search(contacts, search_term):
    search_results = []

    for contact in contacts["contacts"]:
        name_match = re.search(fr"\b{re.escape(search_term)}\b", contact.get("name", ""), flags=re.IGNORECASE)
        phone_match = re.search(fr"\b{re.escape(search_term)}\b", contact.get("phone", ""), flags=re.IGNORECASE)
        email_match = re.search(fr"\b{re.escape(search_term)}\b", contact.get("email", ""), flags=re.IGNORECASE)
        tags_match = any(re.search(fr"\b{re.escape(search_term)}\b", tag, flags=re.IGNORECASE) for tag in contact.get("tags", []))

        if name_match or phone_match or email_match or tags_match:
            search_results.append(contact)

    return search_results

def print_contacts(contacts):
    for contact in contacts["contacts"]:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Tags:", ', '.join(contact["tags"]))
        print()


if __name__ == "__main__":
    file_path = "contacts.json"
    contacts = load_contacts(file_path)
  
    quit = False
    while quit == False:
        print_contacts(contacts)
        choice = input("Choose the mode you want (view by tags/add/update/search/quit): ")

        if choice.lower() == "view by tags":
            tag= input("Name of tags: ")
            filter_contacts_by_tag(contacts, tag)
        elif choice.lower() == "add":
            add_contact(contacts)
        elif choice.lower() == "update":
            update_contact(contacts)
        elif choice.lower() == "search":
            sterm = input("Input search term: ")
            search_results = fuzzy_search(contacts, sterm)
            print("Search results: \n")
            for result in search_results:
                print("Name:", result["name"])
                print("Phone:", result["phone"])
                print("Email:", result["email"])
                print("Tags:", ', '.join(result["tags"]))
                print()
        elif choice.lower() == "quit":
            quit = True
        else:
            print("Invalid choice.")

    save_contacts(file_path, contacts)
        
