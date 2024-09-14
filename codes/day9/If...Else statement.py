a = int(input("Enter your age: "))
print("Your age is: ",a)
print(a<18)
print(a<=18)
print(a>18)
print(a>=18)
print(a!=18)

if(a>18):
    print("You can drive")
else:
    print("You cannot drive")    
appleprice = 10
budget = 200
if(budget-appleprice>50):
    print('alexa, add 1 kg apples to the cart.')
else:
    print("alexa, do not add apples to the cart")