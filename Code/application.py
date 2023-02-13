def set_up():
    print("Welcome to WorkFlow!")
    print("If you already have an account, press 1!")
    print("If you do not have an account, press any other key!")
    choice = input("What would you like to do?:")
    try:
        if choice == 1:
            print("User has an account!")
    except AttributeError or ValueError:
        print("User does not have an account.")
        choice = input("Are you sure you do not have an account? Press 1 to confirm. Press any other key to continue.")
        try:
            if choice == 1:
                print("User has an account (after double checking)!")
        except AttributeError or ValueError:
            print("User wants to continue.")



def run():
    """ All the code in the application is run here. """
    set_up()
    running = True
    while running:
        pass


if __name__ == "__main__":
    """ Program starts here. """
    run()
