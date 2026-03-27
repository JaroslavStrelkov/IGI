def count_numbers_greater_12(numbers):
    #counts the count of numbers greater than twelve
    count = 0

    for num in numbers:
        if num > 12:
            count += 1
    return count