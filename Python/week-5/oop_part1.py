#practice coz this is confusing

class Dog:
    def __init__(self,name,age): #this will be called anytime a new object is created
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age
    def add_one(self,x):
        return x + 1
    def meow(self):
        return "meow"
    def bark(self):
        print("bark")


d = Dog("Tim",34)
d.set_age(5)
print(d.get_age())

d2 = Dog("Max",34)
print(type(d))
d.bark()
print(d.meow())
print(d.add_one(5))