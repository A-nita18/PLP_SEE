#idk where this falls in the coursework but its in this video I'm watching

class Person:
    people_count = 0  #meaning it is the standard for all child classes of this

    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people(cls):
        return cls.people_count 
    
    @classmethod
    def add_person(cls):
        cls.people_count += 1

p1 = Person("Bernice")
print(Person.number_of_people())
p2 = Person("Alex")
print(Person.number_of_people()) #so you can call it by p2 or Person it doesn't matter