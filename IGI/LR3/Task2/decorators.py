def program_repeat(func):
    def wrapper():
        while True:
            func()
            n = input("Do you want to continue? (y/n): ")
            if(n.lower() == "y"):
                continue
            elif (n.lower() == "n"):
                break
            else:
                print("Falsch input!")
    return wrapper