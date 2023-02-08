def verify_account():
    """ Determines whether the user has a pre-existing account. """
    choice = input("Do you have an account? If so, press 1. Otherwise, press 2 to create an account.")
    try:
        if choice == 1:
            # Ask the user to log in
            pass
        elif choice == 2:
            # Ask the user to create a new account
            pass

    except AttributeError or ValueError:
        print("Please choose one of the two options!")


def main():
    """ All program logic is run in this loop."""
    while True:
        print("Test 1 completed - Program running")
        pass


if __name__ == "__main__":
    """ Program starts here. """
    main()
