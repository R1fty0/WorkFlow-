import json


class Class:
    def __init__(self, name, block, file):
        """ A class the user has and its attributes."""
        self.name = name
        self.block = block
        self.file = file


class DataManagement:
    def __init__(self, file):
        """ Stores and retrieves data stored in a json file. """
        self.file = file

    def store_data(self, data):
        """ Stores data in a file. """
        with open(self.file, "w") as f:
            f.write(json.dumps(data))

    def get_data(self):
        """ Returns data from a file. """
        with open(self.file, "r") as f:
            content = f.read()
            return json.loads(content)

    def to_json(self, data):
        """ Converts data into a json accepted format. """
        return data


class TextEssentials:
    def __init__(self):
        self.instructions = ['Press 1 to view your tasks.', 'Press 2 to add a task to your list.',
                             'Press 3 to remove a task from your list.', 'Press 4 to exit the application.']

    def main_menu_text(self) -> int:
        """ Returns the text used in the main menu. """
        for text in self.instructions:
            print(text)
        choice = input("What is your choice?: ")
        try:
            return int(choice)
        except ValueError or AttributeError:
            print("Invalid Option, please try again!")
            self.main_menu_text()
