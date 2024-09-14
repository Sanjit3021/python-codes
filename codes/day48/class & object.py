class Person:
    name='Sanjit'
    occupation="Software Developer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")



a=Person()
b=Person()
c=Person()

b.name="Soumya"
b.occupation="web developer"
c.name="Satya"
c.occupation="Fullstack developer"
a.info()
b.info()
c.info()
