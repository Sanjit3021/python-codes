a=[12,56,32,98,23,76,87,79]
for index,mark in enumerate(a):
    print(index,mark)
    if(index == 3):
        print("I am awesome")
for index,mark in enumerate(a, start=1):
    print(index,mark)