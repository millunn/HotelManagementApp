"""Model for describing room"""
import json

class Room:
    """ Model for room """
    def __init__(self, room_ID: int, type: str, price: int) -> None:
        self.room_ID = room_ID
        self.type = type
        self.price = price
        self.occupied = False
        self.additional_charges = []

    def __str__(self):
        return f"Room number: {self.room_ID}\nRoom type: {self.type}"

    @staticmethod
    def deserialization(string: str) -> "Room":
        """ Deserialize string to room object using json module """
        room = Room(**json.loads(string))
        return room

    @staticmethod
    def load_progress(file_name: str):
        """ Loads the current room list from a file """
        all_rooms = []
        with open(file_name, 'r') as f:
            text = f.read()
            lines = text.split('\n')
            try:
                for i in range(len(lines)):
                    all_rooms.append(Room.deserialization(lines[i]))
            except Exception:
                pass
        
        return all_rooms


