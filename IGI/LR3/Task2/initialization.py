import random
def get_integer():
    #get integer num from user
    while True:
        try:
            num = int(input("Enter number (0 to stop): "))
            return num
        except ValueError:
            print("Falsch input! Enter ineger number")


def input_numbers():
    #filling in the list
    numbers = []
    while True:
            num = get_integer()
            if num == 0:
                break
            numbers.append(num)
    return numbers

def automatic_generation_numbers(size):
    #fill the generator with numbers
    for _ in range(size):
        yield random.randint(-500,500)

def get_size():
    #Get list size from user
    while True:
        try:
            size = int(input())

            if size <= 0:
                print("Falsh input! the size of the list should be >= 1")
                continue
            return size
        except ValueError:
            print("Falsch input! Enter ineger number")

