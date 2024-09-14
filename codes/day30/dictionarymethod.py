ep1={122:54, 123:76, 567:69, 670:69}
ep2={222:67, 566:90}
ep1.update(ep2)
ep1.clear()
ep1.pop(122)
ep1.popitem()
print(ep1)