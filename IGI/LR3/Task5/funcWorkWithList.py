def amount_after_the_minimum(numbers):
    '''sum of the elements arranged up to the elements arranged up to the minimum modulo element'''
    minNum = abs(numbers[0])
    minInx = 0
    for i in range(1, len(numbers)):
        if abs(numbers[i]) < minNum:
            minNum = abs(numbers[i])
            minInx = i
    amount = 0
    for i in range(minInx):
        amount += numbers[i]
    return amount
def mult_positive_num(numbers):
    '''product of the positive elements of the list'''
    result = 1
    hatPositiv = False

    for i in range(len(numbers)):
        if numbers[i] > 0:
            result *= numbers[i]
            hatPositiv = True
    if hatPositiv:
        return result
    else:
        return 0
    
def printList(numbers):
    '''print list'''
    print("List:", numbers)
