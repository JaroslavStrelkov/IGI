#This proogram checks whether the string is a binary number
#LR number 3 "Getting to know the basic python syntax". program version - 1
#Jaroslaw Strelkov did this task on 25.03.2026
from decorators import program_repeat
from check import check_binary
@program_repeat
def main():
    str = input("Enter a string:" )
    if check_binary(str):
        print("This string is a binary number")
    else:
        print("This string is not a binary number")

if __name__ == "__main__":
    main()