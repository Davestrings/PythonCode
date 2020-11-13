import json
from phonebook import *

def main():
    global contacts
    
    file_object = open('backup_file.json', 'r')
    #contacts.update(json.load(file_object))
    contacts.update(json.load(file_object))
    file_object.close()
    
    #collect and store contacts in dictionary    
    store_contacts()
    print(f"contacts = {contacts}")

    #helps to retrieve a contact by a given name
    retrieve_contact()

    file_object = open('backup_file.json', 'w')
    json.dump(contacts, file_object)
    file_object.close()
    
if __name__ == '__main__':
    main()
    
