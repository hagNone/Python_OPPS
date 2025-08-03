"""
Object Oriented Programming is a fundamental concept in Python,
empowering developers to build modular, maintainable, and scalable applications.

OOPs is a way of organizing code that uses objects and classes to represent 
real-world entities and their behavior. In OOPs, object has attributes thing 
that has specific data and can perform certain actions using methods.
Classes are blueprints for creating objects, encapsulating data and behavior
together.

"""

"""
OOPs Concepts in Python
Class in Python
Objects in Python
Polymorphism in Python
Encapsulation in Python
Inheritance in Python
Data Abstraction in Python

"""

"""
Python class
A class is a collection of objects. Classes are blueprints for creating objects. A class 
defines a set of atttributes and methods that the created objects can have

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute


"""

# creating a class

class Dog: # Defines a class named Dog.
    species="Canis" # A class attribute shared by all instances of the class.

    def __init__(self,name,age): # Initializes the name and age attributes when a new object is created.
        self.name=name
        self.age=age

# python objects

class Dog:
    species="canis" # Class attribute shared by all instances.

    def __init__(self,name,age):
        self.name=name
        self.age=age

dog1=Dog("buddu",12) # Creating an instance of the Dog class named dog1 with name "buddu" and age 12.

print(dog1.name) # Accessing instance attributes through the object.
print(dog1.age) # Accessing instance attributes through the object.
print(dog1.species)  # Accessing the class attribute through the object.

"""
self parameter
The self parameter refers to the instance of the class itself. It is used to access variables

self.name: Refers to the name attribute of the object (dog1) calling the method.
"""

class Dog:
    species="canis" 

    def __init__(self,name,age):
        self.name=name
        self.age=age

dog1=Dog("buddu",12)
dog2=Dog("billu",10)

print(dog1.name, dog1.age, dog1.species) 
print(dog2.name, dog2.age, dog2.species)
print(Dog.species)

"""
__init__ method
The __init__ method is a special method in Python classes, known as the constructor.
It is automatically called when a new object of the class is created.
It initializes the object's attributes with the values provided during object creation.
The __init__ method allows you to set initial values for the object's attributes.
self.name and self.age: Instance attributes initialized in the constructor.
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
print(dog1.name)

"""
class and instamce variables

In Python, variables defined in a class can be either class variables or instance variables, 
and understanding the distinction between them is crucial for object-oriented programming.

Class Variables
These are the variables that are shared across all instances of a class. It is defined at the class level,
outside any methods. All objects of the class share the same value for a class variable unless explicitly
overridden in an object.

Instance Variables

Variables that are unique to each instance (object) of a class. These are defined within the __init__ method or other 
instance methods. Each object maintains its own copy of instance variables, independent of other objects.


"""

class Dog:
    species ="Canis" # Class variable shared by all instances.

    def __init__(self,name, age):
        self.name=name # Instance variable unique to each object.
        self.age=age # Instance variable unique to each object.
        self.breed="Labrador" 

dog1=Dog("Buddy", 3) # Instance of Dog class with name "Buddy" and age 3.
dog2=Dog("Max", 5)  # Instance of Dog class with name "Max" and age 5.

print(dog1.name, dog1.age, dog1.species, dog1.breed)  # Accessing instance and class variables for dog1.

dog1.name = "Charlie"  # Changing the name of dog1 instance.
print(dog1.name, dog1.age, dog1.species, dog1.breed)  # Accessing updated instance variables for dog1.

Dog.species = "Canis Familiaris"  # Changing the class variable species for all instances.
print(dog1.species)  # Accessing updated class variable for dog1.
print(dog2.species)  # Accessing class variable for dog2, which reflects


"""
Python Inheritance

Types of Inheritance in Python
1. Single Inheritance: A class inherits from one parent class.
2. Multiple Inheritance: A class inherits from multiple parent classes.
3. Multilevel Inheritance: A class inherits from a parent class, which in turn inherits
4. Hierarchical Inheritance: Multiple classes inherit from a single parent class.from another class.
5. Hybrid Inheritance: A combination of two or more types of inheritance.

"""
#single inheritance
class Dog: # parent class
    def __init__(self, name):
        self.name=name

    def disp_name(self):
        print("Dog name is :", self.name)

class labrador(Dog): # child class inheriting from Dog
    def  sound(self):
        print("Labrador barks")

# multiple inheritance
class GuideDog(labrador):
    def guide(self):
        print(f"{self.name} Guides this way")

# multiple inheritance
class Friendly:
    def greet(self):
        print(f"{self.name} says Hello")

class Goldenretriever(labrador, Friendly): # Inheriting from both labrador and Friendly
    def sound(self):
        print(f"{self.name} loves to play")

# Creating instances of the classes
lab=labrador("buddy")
lab.disp_name()  # Calling method from parent class
lab.sound()  # Calling method from child class

guide_dog = GuideDog("Max")
guide_dog.disp_name()  # Calling method from parent class

guide_dog.guide()  # Calling method from GuideDog class
golden = Goldenretriever("Charlie")
golden.disp_name()  # Calling method from parent class
golden.sound()  # Calling method from Goldenretriever class 
golden.greet()  # Calling method from Friendly class

"""
Polymorphism in Python
Polymorphism is a core concept in object-oriented programming that allows objects of different
classes to be treated as objects of a common superclass.
It enables methods to do different things based on the object it is acting upon, even if they share the same name.
In Python, polymorphism is achieved through method overriding and duck typing.

Types of Polymorphism
Compile-Time Polymorphism: This type of polymorphism is determined during the compilation of the program. 
It allows methods or operators with the same name to behave differently based on their input parameters or usage. 
It is commonly referred to as method or operator overloading.

Run-Time Polymorphism: This type of polymorphism is determined during the execution of the program. 
It occurs when a subclass provides a specific implementation for a method already defined in its parent class, 
commonly known as method overriding.
"""

# run-time polymorphism or method overriding

class Animal:
    def Dog(self,name):
        self.name=name
        print(f"{self.name} is an animal")
    
class Breeds(Animal):
    def Dog(self, name):
        self.name=name
        print(f"{self.name} is a breed of animal")

class Dog(Breeds):
    def Dog(self, name):
        self.name=name
        print(f"{self.name} is a dog breed")

dogs=[Animal(), Breeds(), Dog()]
for dog in dogs:
    dog.Dog("Buddy")

# moethod overriding or run-time polymorphism
class Calcukator:
    def add(self, a, b=0, c=10):
        return a + b + c
    
calc=Calcukator()
print(calc.add(5,10,34))
print(calc.add(5,10))  # Using default value for c
print(calc.add(5))  # Using default values for b and c

"""
Python Encapsulation
Encapsulation is a fundamental concept in object-oriented programming that restricts direct access
to an object's attributes
and methods, allowing them to be accessed only through well-defined interfaces.
It helps in bundling the data (attributes) and methods (functions) that operate on the data into a single unit,
which is the class. Encapsulation promotes data hiding, abstraction, and modularity in code design.

Types of Encapsulation:
Public Members: Accessible from anywhere.
Protected Members: Accessible within the class and its subclasses.
Private Members: Accessible only within the class.
"""

class Car:
    def __init__(self, name, year,vehicalnum):
        self.name=name
        self._year=year
        self.__vehiclenum=vehicalnum

    def getinfo(self):
        return f"Car Name: {self.name}, Year: {self._year}, Vehicle Number: {self.__vehiclenum}"

    #set and get methods for private variablex  
    def get_year(self):
        return self._year
    
    def set_vehiclenum(self, vehiclenum):
        self.__vehiclenum = vehiclenum
        return f"Vehicle number updated to: {self.__vehiclenum}"

# Creating an instance of the Car class
car= Car("Toyota", 2020, "ABC123")
print(car.getinfo())  # Accessing public method to get car information  

print(car.get_year())

car.set_vehiclenum("XYZ456") 
print(car.getinfo())  # Accessing updated vehicle number through public method

"""
Public Members: Easily accessible, such as name.
Protected Members: Used with a single _, such as _breed. Access is discouraged but allowed in subclasses.
Private Members: Used with __, such as __age. Access requires getter and setter methods.
"""

"""
Data Abstraction in Python
Data abstraction is a fundamental concept in object-oriented programming that focuses on hiding 
the complex implementation details of a system
while exposing only the necessary and relevant features to the user.4

Types of Abstraction:
Partial Abstraction: Abstract class contains both abstract and concrete methods.
Full Abstraction: Abstract class contains only abstract methods (like interfaces).
"""

from abc import ABC, abstractmethod

class Dog(ABC):  # Abstract base class
    def __init__(self, name):
        self.name=name
    
    @abstractmethod
    def sound(self):# Abstract method that must be implemented by subclasses
        pass

    def display_name(self):#concrete method
        print(f"Dog name is: {self.name}")

class Labrador(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador Woof!")

class Beagle(Dog):  # Partial Abstraction
    def sound(self):
        print("Beagle Bark!")

# Example Usage
dogs = [Labrador("Buddy"), Beagle("Charlie")]
for dog in dogs:
    dog.display_name()  # Calls concrete method
    dog.sound()  # Calls implemented abstract method


"""
Python static methods
Static methods are methods that belong to a class rather than to any specific instance of the class.
They do not require an instance of the class to be called and can be invoked directly on the class itself.
Static methods are defined using the @staticmethod decorator and do not take the self parameter.
Static methods are typically used for utility functions that do not require access to instance-specific data.
Static methods can be called on the class itself or on instances of the class, but they do not have access to instance-specific data.
Static methods are often used for utility functions that are related to the class but do not require access to instance-specific data.

"""
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# Example usage of static methods
if __name__ == "__main__":
    result_add = MathUtils.add(5, 3)
    result_subtract = MathUtils.subtract(10, 4)
    
    print(f"Addition Result: {result_add}")  # Addition Result: 8
    print(f"Subtraction Result: {result_subtract}")  # Subtraction Result: 6


"""
Constructers in python
In Python, a constructor is a special method that is called automatically when an object is created from a class. 
Its main role is to initialize the object by setting up its attributes or state.

"""

"""
__new__ Method
This method is responsible for creating a new instance of a class. 
It allocates memory and returns the new object. It is called before __init__.
"""
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of MyClass")
        return super(MyClass, cls).__new__(cls)


"""
__init__ Method
This method initializes the newly created instance and is commonly used as a constructor in Python. 
It is called immediately after the object is created by __new__ method and 
is responsible for initializing attributes of the instance.
"""

class Myclass:
    def __init__(self, parameters):
        self.parameters = parameters
        print(f"Initializing MyClass with parameters: {self.parameters}")


"""
Differences Between __init__ and __new__
__new__ method:
Responsible for creating a new instance of the class.
Rarely overridden but useful for customizing object creation and especially in singleton or immutable objects.

__init__ method:
Called immediately after __new__.
Used to initialize the created object.
"""

# types of constructors in python

# Default Constructor
class Car:
    def __init__(self):
        self.make="toyota"
        self.model="corolla"
        self.year=2020

car=Car()
print(f"Car Make: {car.make}, Model: {car.model}, Year: {car.year}")

#parameterized constructor
class Car:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year

car=Car("toyota","corolla",2020)
print(f"Car Name: {car.name}, Model: {car.model}, Year: {car.year}")

"""
python iterators 

An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().


"""
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)