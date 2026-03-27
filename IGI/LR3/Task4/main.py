#This program processes the finished string by performing various operations
#LR number 3 "Getting to know the basic python syntax". program version - 1
#Jaroslaw Strelkov did this task on 25.03.2026
from decorators import program_repeat
from funcWorkWithText import remove_word_witch_first_a, find_word_witch_z, count_upper_lower
@program_repeat
def main():
    str = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, " \
    "whether the pleasure of making a Daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly " \
    "a White Rabbit with pink eyes ran close by her."
    upNum,lowNum = count_upper_lower(str)
    print(f"Count upper symbol in string: {upNum}, count lower symbol in string: {lowNum}")
    wordIndex, word = find_word_witch_z(str)
    print(f"First word in string with 'z': {word}, number this word: {wordIndex}")
    newStr = remove_word_witch_first_a(str)
    print("A string with deleted words starting with the symbol 'a':", newStr)

if __name__ == "__main__":
    main()