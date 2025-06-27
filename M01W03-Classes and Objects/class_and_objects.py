#define a class by the class keyword followed by a name and a colon.
#then use .__init__() to declare which attributes each instance of the class should have
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#classes and instances
#methods: class's functions
#class: blueprint
#instance: an object that's built from a class and contains real data

class Dog:
    species = "Canis familiaris" #class attribute

    def __init__(self, name, age): #name and age are instance attributes
        self.name = name
        self.age = age

    #instance methods
    def description(self):
        return f"{self.name} is {self.age} years old"

    def __str__(self): #print the class's values when type print(miles)
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

#creating a new object from a class
miles = Dog('Miles', 4)
print(miles.name)
print(miles.age)
buddy = Dog('Buddy', 9)
print(buddy.name)
print(buddy.age)
print(buddy.species)

#__str__() and __int__() are dunder methods