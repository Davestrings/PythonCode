def collect_phone_number():
    phone_number = input("type your number: ").strip()
    while not phone_number.isdigit() or len(phone_number) !=11:
        print('invalid phone number')
        phone_number= input("type your number again: ").strip()
    return phone_number

def collect_name():
    name = input("type your name or 'q' to quit ").strip().lower()
    while not name.replace(" ", "").isalpha():
        print('Invalid Name')
        name = input("type your name or 'q' to quit ").strip().lower()
    
    return name 

def store_contact():
    contact = {}
    print(id(contact))
    while True:
        name = collect_name()
        if name == 'quit' or name == 'q':
            break
    #    collect phone number with phone number
        phone_number = collect_phone_number()

        contact[name] = phone_number



def retrieve_contact():
    while True:
        name = collect_name()
        if name == 'quit' or name == 'q':
            break
        try:
            print(name, contact[name])
        except:
            print(name, 'That does not exist')

contact = {}