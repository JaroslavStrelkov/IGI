def continue_program():

    while True:

        answer = input("Continue? (y/n): ").lower()

        if answer == "y":
            return True
        if answer == "n":
            return False

        print("Incorrect input!")