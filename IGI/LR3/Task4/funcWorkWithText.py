def count_upper_lower(str):
    '''counting uppercase and lowercase letters'''
    upNum = 0
    lowNum = 0

    for i in str:
        if i.isupper():
            upNum += 1
        elif i.islower():
            lowNum += 1
    return upNum, lowNum

def find_word_witch_z(str):
    '''find first word with "z"'''
    separators = " ,."
    wordNum = 0
    word = ""

    for i in str:
        if i not in separators:
            word += i
        else:
            if word != " ":
                wordNum += 1
                if "z" in word.lower():
                    return wordNum, word
                word = ""
    return None, None

def remove_word_witch_first_a(str):
    '''delete word in text, wenn sie starting with "a"'''
    separators = " ,."
    newStr = ""
    word = ""

    for i in str:
        if i not in separators:
            word += i
        else:
            if word != " ":
                if word.lower().startswith("a"):
                    word = ""
                    newStr = newStr[:-1]
                newStr += word
                newStr += i
                word = ""
    return newStr
    

