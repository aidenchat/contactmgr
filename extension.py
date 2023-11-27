import re

def print_single_contact(contact):
    print("Name:", contact["name"])
    print("Phone:", contact["phone"])
    print("Email:", contact["email"])
    print("Tags:", ', '.join(contact["tags"]))
    print()

def ask_name(contact):
    name = input("Enter the new name (leave blank to keep it unchanged): ")
    if name:
        contact["name"] = name

def ask_phone(contact):
    phone = input("Enter the new phone number (leave blank to keep it unchanged): ")
    if phone:
        contact["phone"] = phone

def ask_email(contact):
    email = input("Enter the new email address (leave blank to keep it unchanged): ")
    if email:
        contact["email"] = email

def ask_tags(contact):
    tags = input("Enter the new tags (comma-separated, leave blank to keep them unchanged): ")
    if tags:
        new_tags = tags.split(',')
        contact["tags"].extend(new_tags)

def update_contact(contacts):
    search_category = input("Enter the category to search in (name, phone, email, tags): ")
    search_term = input("Enter the search term: ")

    for contact in contacts["contacts"]:
        if search_category == "name":
            search_pattern = re.compile(search_term, re.IGNORECASE)
            if search_pattern.search(contact["name"]):
                ask_phone(contact)
                ask_email(contact)
                ask_tags(contact)
                print("Contact updated successfully.")
                return contact

        elif search_category == "phone":
            search_pattern = re.compile(search_term, re.IGNORECASE)
            if search_pattern.search(contact["phone"]):
                ask_name(contact)
                ask_email(contact)
                ask_tags(contact)
                print("Contact updated successfully.")
                return contact

        elif search_category == "email":
            search_pattern = re.compile(search_term, re.IGNORECASE)
            if search_pattern.search(contact["email"]):
                ask_name(contact)
                ask_phone(contact)
                ask_tags(contact)
                print("Contact updated successfully.")
                return contact

        elif search_category == "tags":
            search_pattern = re.compile(search_term, re.IGNORECASE)
            if any(search_pattern.search(tag) for tag in contact["tags"]):
                ask_name(contact)
                ask_phone(contact)
                ask_email(contact)
                print("Contact updated successfully.")
                return contact
            
    print("Contact not found.")
    return None