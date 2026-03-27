from math import factorial, pow
def func_calculation(x, eps):
    #Calculates the value of a function using a power series expansion
    max = 500
    part = x
    result = 0
    n = 0

    while n < max:
        part = (factorial(2*n) / (pow(4,n) * pow(factorial(n),2) * (2*n + 1))) * (pow(x,(2*n + 1)))
        result += part
        if abs(part) < eps:
            break
        n +=1

    return result, n