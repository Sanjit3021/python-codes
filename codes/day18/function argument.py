def average(a,b):
    print("The average is: ", (a+b)/2)
average(7,5)
def average(a=9, b=1):
    print("The average is: ", (a+b)/2)
average(4,8)
average(b=5)
def average(*numbers):
    sum=0
    for  i in numbers:
        sum=sum+i
    print("Average is: ",sum/len(numbers))

average(3, 5, 6, 7, 8)