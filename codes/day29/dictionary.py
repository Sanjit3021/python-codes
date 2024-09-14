dic = {"Sanjit":"Malik","Soumyajeet":"Panda","sidharth":"Behera"}
print(dic["Sanjit"])
print(dic.get("Sanjit"))
print(dic.keys())
print(dic.values())
for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")
print(dic.items())
for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")