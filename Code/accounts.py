class Account:
    def __init__(self, name, password):
        self.name = name
        self.key = password

    def get_num(self) -> int:
        """ Returns the number of classes the user has. """
        return self.num

    def check_password(self, userInput) -> bool:
        """ Checks to see if the user inputted the correct password. """
        try:
            if str(userInput).upper() == str(self.key).upper():
                print("Password Verified.")
                return True
        except AttributeError:
            print("Incorrect password")
            return False


class Task:
    def __init__(self, name, subject, due_date):
        self.name = name
        self.subject = subject
        self.date = due_date
