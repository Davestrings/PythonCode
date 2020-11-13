import json
from saveContacts import *
def main():
    global contact
    print('created in main.py =', id(contact))
    #try:
    # file_obj = open('backup_file.json', 'r')
    # # contact = json.load(file_obj)
    # contact.update(json.load(file_obj))
    # file_obj.close()
    #except FileNotFoundError:
        #print("No value write")
    
    print('created in main.py =', id(contact))
    
    print('STORAGE MODE')
    store_contact()
    print('created in main.py =', id(contact))
    print(contact)

    print('\n RETRIVAL MODE')
    retrieve_contact()
    
    file_obj = open('backup_file.json', 'w')
    json.dump(contact, file_obj)
    file_obj.close()

if __name__ == '__main__':
    main()
