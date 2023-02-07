""" Functions that will be used in main.py """
from getpass_asterisk.getpass_asterisk import getpass_asterisk

def employee_ID():
    """ Inputs employee ID """
    while True:
        ID = input("Enter ID of the employee: ")
        if ID.isdigit():
            return int(ID)
        print("Must be a integer!")

def employee_password():
    """ Inputs employee password """
    while True:
        password = getpass_asterisk("\nEnter password of the employee: ")
        if password.isalnum():
            return password
        print("Must be an alpha-numerical!")
    
def guest_name():
    """ Inputs guest name """
    while True:
        name = input("Guest's name: ")
        if name.isalpha():
            return name
        print("Must be an alphabetical")

def guest_surname():
    """ Inputs guest surname """
    while True:
        surname = input("Guest's surname: ")
        if surname.isalpha():
            return surname
        print("Must be an alphabetical")

def guest_days_to_stay():
    """ Inputs guest staying days """
    while True:
        days_to_stay = input("Days to stay: ")
        if days_to_stay.isdigit():
            return int(days_to_stay)
        print("Must be a integer")

def guest_loyalty_status():
    """ Inputs guest loyalty status """
    while True:
        loyalty_status = input("Loyalty status (options: '*','**','***' or continue by pressing enter and leaving blank): ")
        if loyalty_status in ('','*','**','***'):
            return loyalty_status
        print("Must be '*','**','***' or left blank and press enter")

def guest_credit_card():
    """ Inputs guest credit card """
    while True:
        card = input("Guest's credit card: ")
        if card.isdigit() and len(card) == 16:
            return card
        print("Must be minimum 16 digits!")

def current_room_pick(room_IDs: list):
    """ Inputs guest current room """
    while True:
        room = input("Current room ID: ")
        if room.isdigit() and int(room) in room_IDs:
            return int(room)
        print(f"Must be a integer and must be in range {room_IDs}")

def new_room_room_pick(room_IDs: list):
    """ Inputs guest desired new room """
    while True:
        room = input("New room ID: ")
        if room.isdigit() and int(room) in room_IDs:
            return int(room)
        print(f"Must be a integer and must be in range {room_IDs}")

def room_pick():
    """ Inputs room number """
    while True:
        room = input("Choose a room number: ")
        if room.isdigit():
            return int(room)
        print("Must be a integer")

def choose_guest_ID():
    """ Inputs guest ID """
    while True:
        guest_ID = input("Guest ID: ")
        if guest_ID.isdigit():
            return int(guest_ID)
        print("Must be a integer")

def choose_rooms_by_type():
    """ Inputs desired answer if room types will be in a descending or ascending order """
    while True:
        rooms_by_type = input("For descending order type: YES, otherwise press enter: ")
        if rooms_by_type.lower() == "yes" or rooms_by_type == "":
            return rooms_by_type
        print("Must be a 'YES' or just click an enter to continue")

def choose_rooms_by_price():
    """ Inputs desired answer if room prices will be in a descending or ascending order """
    while True:
        rooms_by_price = input("For descending order type 'descending', otherwise type 'ascending': ")
        if rooms_by_price.lower() == "descending" or rooms_by_price == "ascending":
            return rooms_by_price
        print("Must be 'descending' or 'ascending'")

def pick_room_service():
    """ Inputs desired room service """
    print("""Pick something from the list below: 

"snickers": 100,
"mars": 100,
"peanuts": 100,
"mixed_nuts": 100,
"beer": 100,
"sparkling_water": 100,
"mineral_water": 100\n

pick one thing and then tap enter""")
    picks = []
    while True:
        room_service = input("Choose from list above: ")
        if room_service.isalpha():
            picks.append(room_service)
            pick_again = input("Want something more? ('yes' or 'no') ")
            while True:
                if pick_again.lower() == 'yes':     
                    room_service = input("Choose from list above: ")
                    picks.append(room_service)
                    pick_again = input("Want something more? ('yes' or 'no') ")
                elif pick_again.lower() == 'no':
                    return picks
                else:
                    print("Must be a 'yes' or 'no'")
                    pick_again = input("Want something more? ('yes' or 'no') ")
