#This proogram calculates the number of numbers greater than 12 in a user-defined list
#LR number 3 "Getting to know the basic python syntax". program version - 1
#Jaroslaw Strelkov did this task on 25.03.2026
from initialization import input_numbers, automatic_generation_numbers, get_size
from counting import count_numbers_greater_12
from decorators import program_repeat

@program_repeat
def main():
    print("Choose a initialisation method:")
    print("1 - Manual input")
    print("2 - Automatic input")
    while True:
        choose = input("Enter choose: ")

        if choose == "1":
            numbers = input_numbers()
            print(f"List: {numbers}")
            break
        elif choose == "2":
            print("Enter the size of the list you want to process")
            size = get_size()
            numbers = automatic_generation_numbers(size)
            print(f"List: {numbers}")
            break
        else:
            print("Falsch input!")

    result = count_numbers_greater_12(numbers)
    print("Count of numbers greater than 12:", result)

if __name__ == "__main__":
    main()