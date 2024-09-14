a = int(input("Enter any value between 5 and 9: "))
if(a<5 and a>9):
    raise ValueError("Value should be between 5 na 9")