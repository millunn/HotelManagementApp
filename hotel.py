"""Model for describing hotel management system"""
from guest import Guest
import operator
from check_info_functions import employee_ID
from datetime import datetime, timedelta , date

class Hotel:
    """Model for hotel management system"""
    invoice = ''

    def __init__(self, employees: list, rooms: list):
        self.employees = employees
        self.rooms = rooms
        self.guests = []
        self.registered_employee = None
        self.registered_guest = None
        self.room_service = {
            "snickers": 100,
            "mars": 80,
            "peanuts": 110,
            "mixed_nuts": 170,
            "beer": 120,
            "sparkling_water": 60,
            "mineral_water": 50}
        self.gym_membership = 500

    def log_in(self, ID: int, password: str) -> bool:
        """ Employee log in """
        for employee in self.employees:
            if ID == employee.ID and password == employee.password:
                print("You've logged in successfully!\n")
                self.registered_employee = employee
                return True
        print("Data invalid")

    def validate_occupancy(self, room_ID: int, guest_ID: int) -> bool:
        """ Validates occupancy of a certain room """
        room_flag = True
        guest_flag = False

        for room in self.rooms:
            if room.room_ID == room_ID:
                room_flag = False
        
        for guest in self.guests:
            if guest.guest_ID == guest_ID:
                guest_flag = True
        
        if room_flag and guest_flag:
            print("Entered guest already has a room!")
            print ("Entered room number doesn't exist!")
            return True
        
        elif guest_flag:
            print("Entered guest already has a room!")
            return True

        elif room_flag:
            print("Entered room number doesn't exist!")
            return True

    def guest_check_in(
        self, guest_ID: int, name: str, surname: str, days_to_stay: int, loyalty_status: str,
         card_number: str, room_ID: int) -> str:
        """ Adds new guest to a hotel """
        if self.validate_occupancy(room_ID, guest_ID):
            return

        for room in self.rooms:
            if room_ID == room.room_ID:
                if not room.occupied:
                    if guest_ID != 0 and name !="" and surname !="" and days_to_stay != 0 \
                        and loyalty_status in ('', '*', '**', '***') and card_number != 0 and room_ID != 0:
                        guest = Guest(
                            guest_ID = guest_ID, name = name,surname = surname, days_to_stay = days_to_stay,
                            loyalty_status = loyalty_status, card_number = card_number, room_assigned = room_ID)
                        self.guests.append(guest)
                        room.occupied = True
                        Hotel.save_progress(guests = self.guests)
                        return f"\n{name} {surname} is our new guest!\n"
                    else:
                        return "\nEntered data not enough!\nFill the rest of blanks\n"
                        
                else:
                    return f"\nRoom {room_ID} is already taken!\n"
                    
    def show_guest_list(self) -> str:
        """ Displays guest list """
        string = ''
        for guest in self.guests:
            string += str(guest)+'\n\n'
        print(f"Guests in hotel: {len(self.guests)}")
        return string

    def validate_guest_update(self, guest_ID: int) -> bool:
        """ Validates registered guest """
        for guest in self.guests:
            if guest.guest_ID == guest_ID:
                self.registered_guest = guest
                return True
        print("Entered guest is not a hotel member!")
        return False

    def guest_update(self, days_to_stay: int, loyalty_status: str, card_number: str) -> None:
        """ Updates guest info """
        if self.validate_guest_update(self.registered_guest.guest_ID):
            self.registered_guest.days_to_stay = days_to_stay
            self.registered_guest.loyalty_status = loyalty_status
            self.registered_guest.set_card_number(card_number)
            print(f"You've successfully updated data for guest: {self.registered_guest.name} {self.registered_guest.surname}")
            Hotel.save_progress(guests = self.guests)
            return

    def guest_check_out(self, room_ID: int) -> None:
        """ Guest signing out from a hotel """
        for room in self.rooms:
            if room_ID == room.room_ID:
                if room.occupied:
                    room.occupied = False
                    for guest in self.guests:
                        if room_ID == guest.room_assigned:
                            print(f"{guest.name} {guest.surname} has successfully checked out from room {room_ID}")
                            print(f"Room {room_ID} is now available!")
                            self.guests.remove(guest)
                            Hotel.save_progress(guests = self.guests)
                            return
                else:
                    print(f"Room {room_ID} is not occupied!")
                    return 
                    
        print("Invalid room ID!")

    def check_if_guest_is_member(self, guest_ID: int) -> bool:
        """ Validates registered guest """
        for guest in self.guests:
            if guest.guest_ID == guest_ID:
                return True
        print("Entered guest is not a hotel member!")
        return False

    def check_if_room_exists(self, room_ID: int) -> bool:
        """ Checks room's existence """
        for room in self.rooms: 
            if room.room_ID == room_ID:
                return True
        print(f"Rooom {room_ID} doesn't exist!")
        return False

    def check_if_rooms_are_occupied(self, current_room, new_room)-> bool:
        """ Checks room's occupancy """
        current_room_flag = False
        new_room_flag = False

        for room in self.rooms:
            if room.room_ID == current_room and room.occupied:
                current_room_flag = True
            
            elif room.room_ID == current_room and not room.occupied:
                print(f"Room {current_room} is not occupied and therefore cannot be disoccupied!")

            elif room.room_ID == new_room and not room.occupied:
                new_room_flag = True
                
            elif room.room_ID == new_room and room.occupied:
                print(f"Room {new_room} is occupied, pick another room!")
                
        if current_room_flag and new_room_flag:
            return True 

    def change_room(self, guest_ID, current_room, new_room) -> str:
        """ Switches guest room """
        if self.check_if_guest_is_member(guest_ID):
            if self.check_if_room_exists(current_room) and self.check_if_room_exists(new_room):
                if self.check_if_rooms_are_occupied(current_room, new_room):

                        for guest in self.guests:
                            if guest_ID == guest.guest_ID:
                                if guest.room_assigned == current_room:
                                    guest.room_assigned = new_room
                                    for room in self.rooms:
                                        if room.room_ID == current_room:
                                            room.occupied = False
                                        if room.room_ID == new_room:
                                            room.occupied = True
                                            Hotel.save_progress(guests = self.guests)
                                            print(f"Guest {guest.name} {guest.surname} has successfully switched rooms from {current_room} to {new_room}")
                                            return
                                else:
                                    print(f"Guest {guest.name} {guest.surname} is not in room {current_room}\nPut the correct room ID!")
                                    return
    
    def show_receptionist(self) -> str:
        """ Displays info of a current receptionist """
        if self.registered_employee != None:
            return f"{self.registered_employee.name} {self.registered_employee.surname}"

    def show_room_list(self) -> str:
        """ Displays rooms info """
        room_string = ''
        for room in self.rooms:
            room_string += str(room) + '\n\n'
        return room_string

    def show_rooms_filtered_by_type(self, luxury_first: str = None) -> str:
        """ Displays rooms filtered by type """
        room_string = ''
        if luxury_first == None or luxury_first == "":
            for room in self.rooms:
                room_string += str(room.room_ID) + ' --> ' + str(room.type) + '\n\n'
            return room_string
        elif luxury_first.lower() == "yes":
            sorted_rooms = sorted(self.rooms, key=operator.attrgetter("room_ID"), reverse=True)
            for room in sorted_rooms:
                room_string += str(room.room_ID) + ' --> ' + str(room.type) + '\n\n'
            return room_string
        else:
            return "Invalid data input\nMust be 'yes' or leave it unfilled"

    def show_rooms_filtered_by_price(self, order: str) -> str:
        """ Displays rooms filtered by price """
        room_string = ''
        match order.lower():
            case "ascending":
                for room in self.rooms:
                    room_string += str(room.room_ID) + ' --> ' + str(room.price) + ' RSD/day' + '\n\n'
                return room_string
            case "descending":
                sorted_rooms = sorted(self.rooms, key=operator.attrgetter("price"), reverse=True)
                for room in sorted_rooms:
                    room_string += str(room.room_ID) + ' --> ' + str(room.price) + ' RSD/day' + '\n\n'
                return room_string
            case other:
                return ("Invalid data input\nMust be 'ascending' or 'descending' order")

    def show_available_rooms(self) -> str:
        """ Displays available rooms """
        room_string = ''
        for room in self.rooms:
            if not room.occupied:
                room_string += str(room) + '\n\n'
        return room_string

    def pricelist(self) -> str:
        """ Displays rooms pricelist """
        prices = ''
        for room in self.rooms:
            prices += str(room.type)+' ----> ' + str(room.price) + ' RSD/day' + '\n\n'
        return prices

    def add_room_service(self, room_ID: int, room_service: list) -> None:
        """ Adds room service """
        for room in self.rooms:
            if room_ID == room.room_ID:
                if room.occupied:
                    for item in room_service:
                        if item in self.room_service.keys():
                            room.additional_charges += [item]
                            print(f"You've successfully added {item} to room's {room_ID} bill")
                        else:
                            print(f"Item {item} is not available in our room service and therefore cannot be added")
                    return
                else:
                    print(f"Room {room_ID} is not occupied and therefore cannot have additional charges!")
                    return                
        return "Invalid room ID!"

    def become_gym_member(self, room_ID: int) -> None:
        """ Assigns gym membership """
        for room in self.rooms:
            if room_ID == room.room_ID:
                if room.occupied:
                    room.additional_charges += ["gym"]
                    return f"You've successfully added gym_membership to room's {room_ID} bill"
                else:
                    return f"Room {room_ID} is not occupied and therefore cannot have additional charges!"
                     
        return "Invalid room ID!"

    def check_loyalty_status(self, status: str = None) -> float:
        """ Checks loyalty status """
        match status:
            case '*':
                print("Your status is Silver! Your account will be reduced by 10%")
                return 0.9
            case '**':
                print("Your status is Gold! Your account will be reduced by 15%")
                return 0.85
            case '***':
                print("Your status is Platinum! Your account will be reduced by 20%")
                return 0.80
            case None:
                return 1
            case other:
                print("Discount is not applied\nYou must choose between '*' or '**' or '***'")
                return 1
        
    def issue_invoice(self, room_ID: int) -> str:
        """ Issues a final bill """
        amount = 0
        for room in self.rooms:
            if room_ID == room.room_ID:
                for guest in self.guests:
                    if guest.room_assigned == room_ID:
                        guest_loyalty_status = self.check_loyalty_status(guest.loyalty_status)
                        amount = room.price * guest.days_to_stay
                        if guest_loyalty_status:
                            amount *= guest_loyalty_status
                        if room.additional_charges != []:
                            for item in room.additional_charges:
                                if item == "gym":
                                    amount += self.gym_membership
                                if item in self.room_service:
                                    amount += self.room_service[item]
                            self.invoice = f"\n-------INVOICE----------\n\nRoom number: {room_ID}\n\nCheck in date: {date.today() - timedelta(days = guest.days_to_stay)}\n\n" \
                                           f"Room type: {room.type}\n\nDays: {guest.days_to_stay}\n\nAmount: {round(amount,2)} RSD\n\n" \
                                           f"Issued by: {self.registered_employee.name} {self.registered_employee.surname}\n\nDiscount: {round((1-guest_loyalty_status)*100)} %\n\n" \
                                           f"Additional charges: {room.additional_charges}\n\nDate of issue: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n------------------------\n"
                        else:
                            self.invoice = f"\n--------INVOICE---------\n\nRoom number: {room_ID}\n\nCheck in date: {date.today() - timedelta(days = guest.days_to_stay)}\n\n" \
                                           f"Room type: {room.type}\n\nDays: {guest.days_to_stay}\n\nAmount: {amount} RSD\n\nDiscount: {round((1-guest_loyalty_status)*100)} %\n\n" \
                                           f"Issued by: {self.registered_employee.name} {self.registered_employee.surname}\n\nDate of issue: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n------------------------\n"
                        self.save_invoice_as_txt()
                        return self.invoice

                return f"Room {room_ID} is not occupied!"

        return "Invalid room ID!"

    def log_out(self) -> str:
        """ Logs out """
        if self.registered_employee != None:
            self.registered_employee = None
            return "You've successfully logged out"
            
    def find_next_id(self) -> int:
        """ Finds next ID in guest list """
        if self.guests != []:
            guest_iDs = []
            for guest in self.guests:
                guest_iDs.append(guest.guest_ID)
            guest_iDs.sort(reverse=True)
            next_ID = guest_iDs[0] + 1
            return next_ID
        return 1

    def occupy_room_by_guests_data(self) -> None:
        """ Occupies rooms in class Room by matching guest data loaded from files - changing flag's value """
        room_IDs = []
        for guest in self.guests:
            room_IDs.append(guest.room_assigned)
        for room in self.rooms:
            if room.room_ID in room_IDs:
                room.occupied = True

    def find_room_IDs(self) -> list:
        room_IDs = []
        for room in self.rooms:
            room_IDs.append(room.room_ID)
        return room_IDs

    @staticmethod
    def save_progress(guests: list) -> None:
        """ Saves the last guest progress """
        with open("guests.txt", 'w') as f:
            for guest in guests:
                f.write(f"{guest.serialization()}\n")

    @staticmethod
    def check_guest_ID_before_loading_from_file(guest_list: list) -> list:
        """ Checks guest ID uniqueness before loading data from file """
        IDs_list = []
        for guest in guest_list:
            IDs_list.append(guest.guest_ID)
        duplicates = []
        for element in IDs_list:
            if IDs_list.count(element) > 1:
                duplicates.append(element)
        return duplicates

    def check_room_ID_before_loading_from_file(self) -> list:
        """ Checks room's existence and uniqueness before loading data from file """
        room_IDs_list = []
        for guest in self.guests: 
            room_IDs_list.append(guest.room_assigned)
        for ID in room_IDs_list:
            if ID not in self.find_room_IDs():
                print(f"\n\nCould not load data! Room {ID} non-existent\n\n")
                return [0]
        duplicates = []
        for element in room_IDs_list:
            if room_IDs_list.count(element) > 1:
                duplicates.append(element)
        if duplicates != []:
            print(f"\n\nCould not load data! There are certain room ID duplicates: {set(duplicates)}\n\n")
            return duplicates
        return duplicates

    @staticmethod
    def load_progress(file_name: str) -> list:
        """ Loads the current guest list from a file """
        all_guests = []
        with open(file_name, 'r') as f:
            text = f.read()
            lines = text.split('\n')
            try:
                for i in range(len(lines)):
                    all_guests.append(Guest.deserialization(lines[i]))
            except Exception:
                pass
        duplicate_IDs = Hotel.check_guest_ID_before_loading_from_file(all_guests)
        if duplicate_IDs == []:
            return all_guests
        print(f"\n\nCould not load data! There are certain guest ID duplicates: {set(duplicate_IDs)}\n\n")
        return 

    def get_employee_password(self, ID) -> int:
        """ Gets employee password """
        for employee in self.employees:
            if ID == employee.ID:
                return employee.password

    def get_forgotten_password(self, mail, ID) -> None:
        """ Creates mail subject and body for a forgotten password, sends if it's called """
        import smtplib
        import ssl
        from email.message import EmailMessage

        email_sender = "m7testpy@gmail.com"
        email_password = "vfsk dpsh piqi ztbg"
        email_receiver = mail
        subject = "Forgotten password"
        body = f"Your password: {self.get_employee_password(ID)}"
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("You've successfully sent an email!")

    def send_forgotten_password(self) -> None:
        """ Sends employee's password to a mail if forgotten """
        print("Before we start - ", end='')
        question = input("Did you forget your password: (Y / N, to continue press 'N') ")
        while True:
            if question.lower() == 'y':
                emp_ID = employee_ID()
                mail = input("Enter a mail where you want to receive forgotten password: ")
                self.get_forgotten_password(mail = mail, ID = emp_ID)
                return
            elif question.lower() == 'n':
                return
            else:
                print("Must be 'Y' or 'N'")
                question = input("Did you forget your password: (Y / N) ")

    def save_invoice_as_txt(self) -> None:
        """ Creates text file invoice when called """
        with open("invoice.txt", 'w') as f:
            f.write(f"{self.invoice}")



