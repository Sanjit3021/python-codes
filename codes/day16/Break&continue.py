for i in range(15):
    if(i==10):
        break
    print("5 X",i+1, "=", 5*(i+1))
print("Goes out of loop")
for i in range(15):
    if(i==10):
        print("skipthe iteration")
        continue
    print("5 X",i, "=", 5*i)
i=0
while True:
    print(i)
    i=i+1
    if(i%100)==0:
      break