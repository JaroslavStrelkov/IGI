def exit_from_the_loop():
    '''Ask user to repeat program'''
    while True:
        n = input("Do you want to continue? (y/n): ")
        if(n.lower() == "y"):
            return True
        elif (n.lower() == "n"):
            return False
        
        else:
            print("Falsch input!")