x=5
print(x)


def hello():
    global x
    x=7
    print(f"the local x is {x}")
    print("Sanjit")


print(f"The global x is {x}")
hello()
print(x)
