"""Model for describing employee"""
import json

class Employee:
    """ Model for employee """
    def __init__(self, name: str, surname: str, ID, password: str):
        self.name = name
        self.surname = surname
        self.ID = ID
        self.__password = password

    def __str__(self):
        return f'Name Surname: {self.name} {self.surname}\nID: {self.ID}\nPassword: {self.password()}'

    @property
    def password(self):
        """ Gets employee password """
        return self.__password

    @staticmethod
    def deserialization(string: str) -> "Employee":
        """ Deserialize string to employee object using json module """
        employee = Employee(**json.loads(string))
        return employee

    @staticmethod
    def load_progress(file_name: str):
        """ Loads the current employee list from a file """
        all_employess = []
        with open(file_name, 'r') as f:
            text = f.read()
            lines = text.split('\n')
            try:
                for i in range(len(lines)):
                    all_employess.append(Employee.deserialization(lines[i]))
            except Exception:
                pass

        return all_employess







