import random
def get_float():
    #get float num from user
    
    while True:
        try:
            num = float(input("Enter number: "))
            return num
        except ValueError:
            print("Falsch input! Enter float number")


def input_numbers(size):
    #filling in the list
    numbers = []
    for i in range(size):
        num = get_float()
        numbers.append(num)
    return numbers

def automatic_generation_numbers(size):
    #fill the generator with numbers
    numbers = []
    for _ in range(size):
        yield round(random.uniform(-200.0, 200.0), 2)

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

