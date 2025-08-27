#activity 1
class Device:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
        
    def device_info(self):
        print(self.name,self.brand)

class Smartphone(Device):
    def __init__(self, name, brand,battery):
        super().__init__(name, brand)
        self.__battery = battery

    def use_phone(self,hours):
        self.__battery -= hours*10
        if self.__battery < 0 :
            self.__battery = 0
        print(f"You have used phone for {hours} hours, {self.__battery} percent of battery left")
    
    def charge(self,hours):
        self.__battery += hours*20
        if self.__battery > 100:
            self.__battery = 100
        print(f"Phone has charged for {hours} hours, phone is at {self.__battery} percent")

    def get_battery(self):
        print(self.__battery," percent")

phone1 = Smartphone("Tylang", "Samsung", 100)
device2 = Device("Fridge","Samsung")
phone1.use_phone(6)
device2.device_info()
#activity 2

class Animals:
    def move(self):
        print("All animals move")

class Kangaroo(Animals):
    def move(self):
        print("Kangaroos hop")

class Hippo(Animals):
    def move(self):
        print("Hippos swim and run very fast")

class Eagle(Animals):
    def move(self):
        print("Nothing flys like an eagle")

animals = [Kangaroo(),Hippo(),Eagle()]

for animal in animals:
    animal.move()
