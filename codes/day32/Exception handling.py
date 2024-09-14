a = input("Enter the number:")
print(f"Multiplication tableof {a} is:")
try:
  for i in range(1,11):
   print(f"{int(a)} x {i} = {int(a)*i}")
except:
  print("Invalid Input")
print("Some imp lines of code")
print("End of  program")
try:
    num=int(input("Enter an Integer:"))
    a = [6,3]
    print(a[num])
except ValueError:
    print("The number entered is not an integer")
except IndexError:
    print("Index Error")