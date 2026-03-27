#This proogram make product of the positive elements of the list 
#and sum of the elements arranged up to the elements arranged up to the minimum modulo element
#LR number 3 "Getting to know the basic python syntax". program version - 1
#Jaroslaw Strelkov did this task on 25.03.2026
from initialization import input_numbers, automatic_generation_numbers, get_size
from funcWorkWithList import printList, amount_after_the_minimum, mult_positive_num
from decorators import program_repeat

@program_repeat
def main():
    print("Enter the size of the list you want to process")
    size = get_size()
    print("Choose a initialisation method:")
    print("1 - Manual input")
    print("2 - Automatic input")
    while True:
        choose = input("Enter choose: ")

        if choose == "1":
            numbers = input_numbers(size)
            printList(numbers)
            break
        elif choose == "2":
            numbers = automatic_generation_numbers(size)
            printList(numbers)
            break
        else:
            print("Falsch input!")
    product = mult_positive_num(numbers)
    print("The product of the positive elements of the list:", product)
    amount = amount_after_the_minimum(numbers) 
    print("The sum of the elements arranged up to the elements arranged up to the minimum modulo element:", amount)

if __name__ == "__main__":
    main()