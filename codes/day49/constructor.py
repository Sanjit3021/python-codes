class Person:
    def __init__(self, n, o):
        print("hey I am a person")
        self.name=n
        self.occ=o

    def info(self):
        print(f"{self.name} is a {self.occ}")
    

a=Person("Sanjit","Game developer")
b=Person("Soumya","Web developer")
a.info()
b.info()