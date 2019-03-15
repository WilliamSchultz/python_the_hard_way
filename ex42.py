## Animal is-a object
class Animal(object):
    pass

## is-a animal 
class Dog(Animal):

    def __init__(self, name):
        ##
        self.name = name

## is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##
        self.name = name

## has-a object
class Person(object):

    def __init__(self, name):
        ##Person has-a name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

## is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ##
        self.salary = salary

## has-a object
class Fish(object):
    pass

## is-a fish
class Salmon(Fish):
    pass

## is-a fish
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## is-a cat
satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 12000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut
