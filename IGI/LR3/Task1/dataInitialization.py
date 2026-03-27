
def floatValue(word):
    #Get float value from user with validation
    while True:
        try:
            value = float(input(word))
            return value
        except:
            print("Falsch input!")



def input_values():
    #Get x and eps from user
    while True:
        x = floatValue("Enter x (|x| < 1): ")
        if -1 < x < 1:
            break
        print("x in is limited from -1 to 1!")

    eps = floatValue("Enter eps: ")
    return x, eps
    