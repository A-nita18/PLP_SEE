#starting to add up

class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    
    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour
    def show(self):
        print(f"I am {self.name} {self.age} years old and I am {self.colour}")
    def speak(self):
        print("Meow") 

class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Collins", 24)
p.show()
c = Cat("Leon", 7, "Gold")
c.show()
d = Dog("Cate",9)
d.speak