class Parent:
    hair_color = "brown"
    speaks = ['English']

class Child(Parent): #child's hair_color is also "brown" without explicitly defining that
    hair_color = "purple" #override
    def __init__(self):
        super().__init__()
        self.speaks.append('German') #extend

#child classes can override or extend the attributes and methods of parent classes

#EXAMPLE: DOG PARK
class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

#to determine which class a given object belongs to
miles = Dog('Miles', 2, 'Golden')
type(miles)
#determine if miles is also an instance of the Dog class
isinstance(miles, Dog)

class JackRussellTerrier(Dog):
    def __init__(self, name, age, breed = 'JackRussellTerrier'):
       self.name = name
       self.age = age


    def speak(self, sound = 'Arf'):
        return f"{self.name} says {sound}" #overide a method

miles = JackRussellTerrier('Miles', 4)
miles.speak()
