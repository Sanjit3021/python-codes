# Python program to display the Fibonacci sequence

def f(n):
   if n <= 1:
       return n
   else:
       return(f(n-1) + f(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(f(i))