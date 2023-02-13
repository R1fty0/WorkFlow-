import json


class Account:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        if password is None:
            self.set_password()

    def check_password(self, user_input) -> bool:
        """ Checks to see if the user inputted their password correctly. Returns true if they did and false if they didn't. """
        try:
            if str(user_input) == str(self.password):
                return True
        except AttributeError:
            if int(user_input) == int(self.password):
                return True
        else:
            return False

    def set_password(self):
        """ Allows the user to set a password for their account. """
        password = input("What would like your password to be?: ")
        self.password = password


class Subject:
    def __init__(self, name, block, data_file):
        """ Contains a subject/class's attributes."""
        self.name = name
        self.block = block
        self.file = data_file


class JsonDataManagement:
    def __init__(self, file):
        """ Stores and retrieves data stored in a given json file. """
        self.file = file

    def store_data(self, data):
        """ Stores data in a json file. """
        with open(self.file, "w") as f:
            f.write(json.dumps(data))

    def get_data(self):
        """ Retrieves data stored in a json file. """
        with open(self.file, "r") as f:
            content = f.read()
            return json.loads(content)


class Text:
    def __init__(self):
        """ Contains all the text shown to the user while the application is running. """
        self.menu_instructions = ['Press 1 to view your tasks.', 'Press 2 to add a task to your list.',
                                  'Press 3 to remove a task from your list.', 'Press 4 to exit the application.']

    def main_menu(self) -> int:
        """ Runs the main menu and returns the choice the user made from the menu's options.  """
        for text in self.menu_instructions:
            print(text)  # Prints menu and options
        choice = input("What is your choice?: ")

        try:
            return int(choice)  # Returns the user's choice if they inputted an integer.
        except ValueError or AttributeError:
            print("Invalid Option, please try again!")
            self.main_menu()



