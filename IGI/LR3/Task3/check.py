def check_binary(str):
    #check binary string or no
    if not str:
        print("String is empty")
        return False
    for i in str:
        if i != "0" and i != "1":
            return False
    return True
    