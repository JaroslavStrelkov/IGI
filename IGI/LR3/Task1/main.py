#This program calculates the value of a function using a power series expansion.
#LR number 3 "Getting to know the basic python syntax". program version - 1
#Jaroslaw Strelkov did this task on 25.03.2026
from math import asin
from dataInitialization import input_values
from exit import exit_from_the_loop
from calculation import func_calculation

def main():
    while True:
        x, eps = input_values()
        
        res, n = func_calculation(x, eps)
        from math import asin

        print("-"*74)
        print(f"| {'x':^8} | {'n':^6} | {'F(x)':^18} | {'Math F(x)':^18} | {'eps':^8} |")
        print("-"*74)
        print(f"| {x:^8} | {n:^6} | {res:^18} | {asin(x):^18} | {eps:^8} |")
        print("-"*74)


        if not exit_from_the_loop():
            break

if __name__ == "__main__":
    main()