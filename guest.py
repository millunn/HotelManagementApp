"""Model for describing guest"""
import json

class Guest:
    """ Model for guest """
    def __init__(self, guest_ID: int, name: str, surname: str, days_to_stay: int, card_number: str, loyalty_status: str = None, room_assigned: int = None):
        self.__guest_ID = guest_ID
        self.name = name
        self.surname = surname
        self.days_to_stay = days_to_stay
        self.__card_number = card_number
        self.loyalty_status = loyalty_status
        self.room_assigned = room_assigned
    
    def __str__(self):
        return f"Name_surname: {self.name} {self.surname}\nStaying days: {self.days_to_stay}\nLoyalty status: {self.loyalty_status}\nRoom assigned: {self.room_assigned}"

    @property
    def guest_ID(self):
        """ Gets guest ID """
        return self.__guest_ID
    
    @property
    def card_number(self):
        """ Gets guest credit card number """
        return self.__card_number

    def set_card_number(self, new_card_number):
        """ Sets guest credit card number """
        self.__card_number = new_card_number

    def serialization(self) -> str:
        """ Serialize using special method dict to make a string of an object guest """
        string = ""
        dictionary = self.__dict__
        corrected_dict = {k.replace('_Guest__card_number', 'card_number'): v for k, v in dictionary.items()}
        corrected_dict_2 = {k.replace('_Guest__guest_ID', 'guest_ID'): v for k, v in corrected_dict.items()}
        string += json.dumps(corrected_dict_2, default=str)
        return string

    @staticmethod
    def deserialization(string: str) -> "Guest":
        """ Deserialize string to guest object using json module """
        guest = Guest(**json.loads(string))
        return guest