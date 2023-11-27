import re
print("hi")
# output hi
# vault for past versions
# old update_contact
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