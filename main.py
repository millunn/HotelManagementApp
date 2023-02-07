from hotel import Hotel
from employee import Employee
from room import Room
from check_info_functions import guest_name, room_pick, guest_surname, guest_loyalty_status, guest_days_to_stay, \
                 guest_credit_card, choose_guest_ID, employee_ID, employee_password, choose_rooms_by_type, \
                 choose_rooms_by_price, pick_room_service, current_room_pick, new_room_room_pick

if __name__ == "__main__":

    h = Hotel(employees = Employee.load_progress("employees.txt"), rooms = Room.load_progress("rooms.txt"))
    h.guests = h.load_progress("guests.txt")
    if h.check_room_ID_before_loading_from_file() == []:

        h.occupy_room_by_guests_data()
        print("\n\n*** Welcome to Hotel Lowry ***\n\n")
        if h.send_forgotten_password():
            print("\n\nPlease log in:\n\n")
            if h.log_in(employee_ID(), employee_password()):
                print("""\nChoose from the following options:\n
            A. Admission/Departure
            B. Guests
            C. Rooms
            D. Additional features
            E. Reception

            type 'End' to quit the app.\n""")

                enter_option = input("Enter the desired option: ")
                
                while enter_option.lower() != "end":
                    match enter_option.lower():     
                        case 'a':
                            print("\n\n================ADMISSION PAGE===============\n\n")
                            print("""\nChoose from the following options:\n
                            A1. Guest check-in
                            A2. Guest check-out
                            type 'End' to quit the app.\n""")
                            print("\n\n================ADMISSION PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a1-a2)\nfor cancellation enter 'End': ") 
                        case 'b':
                            print("\n\n================GUEST PAGE===============\n\n")
                            print("""\nChoose from the following options:\n
                            B1. Display guest list
                            B2. Update guest data
                            B3. Switch rooms\n
                            type 'End' to quit the app.\n""")
                            print("\n\n================GUEST PAGE===============\n\n")
                            enter_option=input("Enter the desired option (b1-b3)\nfor cancellation enter 'End': ")
                        case 'c':
                            print("\n\n================ROOMS PAGE===============\n\n")
                            print("""\nChoose from the following options:\n
                            C1. Display room list
                            C2. Display room list filtered by type
                            C3. Display room list filtered by price
                            C4. Display available rooms
                            C5. Display room pricelist\n    
                            type 'End' to quit the app.\n""")
                            print("\n\n================ROOMS PAGE===============\n\n")
                            enter_option=input("Enter the desired option (c1-c5)\nfor cancellation enter 'End': ")
                        case 'd':
                            print("\n\n================ADDITTIONAL FEATURES PAGE===============\n\n")
                            print("""\nChoose from the following options:\n
                            D1. Room service
                            D2. Gym membership\n
                            type 'End' to quit the app.\n""")
                            print("\n\n================ADDITTIONAL FEATURES PAGE===============\n\n")
                            enter_option=input("Enter the desired option (d1-d2)\nfor cancellation enter 'End': ")
                        case 'e':
                            print("\n\n================RECEPTION PAGE===============\n\n")
                            print("""\nChoose from the following options:\n
                            E1. Show receptionist info
                            E2. Log out\n
                            type 'End' to quit the app.\n""")
                            print("\n\n================RECEPTION PAGE===============\n\n")
                            enter_option=input("Enter the desired option (e1-e2)\nfor cancellation enter 'End': ")
                        case 'a1':
                            print("\n\n================ADMISSION PAGE===============\n\n")
                            print(h.guest_check_in(
                                guest_ID = h.find_next_id(), name = guest_name(), surname = guest_surname(), days_to_stay = guest_days_to_stay(),
                                loyalty_status = guest_loyalty_status(), card_number = guest_credit_card(), room_ID = room_pick()))
                            print("\n\n================ADMISSION PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ") 
                        case 'a2':
                            print("\n\n================ADMISSION PAGE===============\n\n")
                            room_ID = room_pick()
                            print()
                            print(h.issue_invoice(room_ID))
                            h.guest_check_out(room_ID)
                            print("\n\n================ADMISSION PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")
                        case 'b1':
                            print("\n\n================GUEST PAGE===============\n\n")
                            print(h.show_guest_list())
                            print("\n\n================GUEST PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")
                        case 'b2':
                            print("\n\n================GUEST PAGE===============\n\n")
                            if h.validate_guest_update(choose_guest_ID()):
                                h.guest_update(
                                    days_to_stay = guest_days_to_stay(), loyalty_status = guest_loyalty_status(),
                                    card_number = guest_credit_card())
                            print("\n\n================GUEST PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")
                        case 'b3':
                            print("\n\n================GUEST PAGE===============\n\n")
                            h.change_room(choose_guest_ID(), current_room_pick(h.find_room_IDs()), new_room_room_pick(h.find_room_IDs()))
                            print("\n\n================GUEST PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ") 
                        case 'c1':
                            print("\n\n================ROOMS PAGE===============\n\n")
                            print(h.show_room_list())
                            print("\n\n================ROOMS PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")
                        case 'c2':
                            print("\n\n================ROOMS PAGE===============\n\n")
                            print(h.show_rooms_filtered_by_type(choose_rooms_by_type()))
                            print("\n\n================ROOMS PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")
                        case 'c3':
                            print("\n\n================ROOMS PAGE===============\n\n")
                            print(h.show_rooms_filtered_by_price(choose_rooms_by_price()))
                            print("\n\n================ROOMS PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")
                        case 'c4':
                            print("\n\n================ROOMS PAGE===============\n\n")
                            print("\nAvailable rooms are:\n")
                            print(h.show_available_rooms())
                            print("\n\n================ROOMS PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")
                        case 'c5':
                            print("\n\n================ROOMS PAGE===============\n\n")
                            print(h.pricelist())
                            print("\n\n================ROOMS PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")    
                        case 'd1':
                            print("\n\n================ADDITTIONAL FEATURES PAGE===============\n\n")
                            h.add_room_service(room_ID = room_pick(), room_service = pick_room_service())
                            print("\n\n================ADDITTIONAL FEATURES PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")
                        case 'd2':
                            print("\n\n================ADDITTIONAL FEATURES PAGE===============\n\n")
                            print(h.become_gym_member(room_ID = room_pick()))
                            print("\n\n================ADDITTIONAL FEATURES PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")
                        case 'e1':
                            print("\n\n================RECEPTION PAGE===============\n\n")
                            print("\nCurrent receptionist:\n")
                            print(h.show_receptionist())
                            print("\n\n================RECEPTION PAGE===============\n\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")
                        case 'e2':
                            print("\n\n================RECEPTION PAGE===============\n\n")
                            print(h.log_out())
                            print("\n\n================RECEPTION PAGE===============\n\n")
                            break
                        case other:
                            print("\nWrong enter!\nTry again\n")
                            enter_option=input("Enter the desired option (a-e)\nfor cancellation enter 'End': ")

