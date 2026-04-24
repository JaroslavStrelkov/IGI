def get_float(message):

    while True:
        try:
            return float(input(message))

        except ValueError:
            print("Incorrect input!")


def input_values():

    while True:
        x = get_float("Enter x (-1 < x < 1): ")
        if -1 < x < 1:
            break
        print("x must be in range (-1, 1)")

    while True:
        eps = get_float("Enter eps: ")
        if eps > 0:
            break
        print("eps must be greater than 0")
    return x, eps