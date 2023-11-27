import json
import re
from extension import *

file_path = "contacts.json"
def load_contacts(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_contacts(file_path, contacts):
    with open(file_path, 'w') as file:
        json.dump(contacts, file, indent=2)
                
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

def print_contacts(contacts):
    for contact in contacts["contacts"]:
        print_single_contact(contact)

if __name__ == "__main__":
    file_path = "contacts.json"
    contacts = load_contacts(file_path)

    quit = False
    #print_contacts(contacts)
    while quit == False:
        choice = input("Choose the mode you want (view by tags/add/update/search/delete/quit): ")

        if choice.lower() == "view by tags":
            contacts = load_contacts(file_path)
            tag = input("Input tag: ")
            filter_contacts_by_tag(contacts, tag)
        elif choice.lower() == "add":
            add_contact(contacts)
            save_contacts(file_path, contacts)
        elif choice.lower() == "update":
            contacts = load_contacts(file_path)
            updated_contact = update_contact(contacts)
            if updated_contact:
                print("Updated Contact:")
                print_single_contact(updated_contact)
            save_contacts(file_path, contacts)
        elif choice.lower() == "search":
            sterm = input("Input search term: ")
            search_results = fuzzy_search(contacts, sterm)
            print("Search results: \n")
            for result in search_results:
                print_single_contact(result)
        elif choice.lower() == "delete":
            contacts = load_contacts(file_path)
            deleted_contact = delete_contact(contacts)
            if deleted_contact:
                print("Deleted Contact:")
                print_single_contact(deleted_contact)
            save_contacts(file_path, contacts)
        elif choice.lower() == "quit":
            quit = True
        else:
            print("Invalid choice.")

    save_contacts(file_path, contacts)

