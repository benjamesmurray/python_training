#OOP

#Library:
#Each library in Python contains a huge number of useful modules that you can import.

#Module:
#A module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

#Class: e.g. Dog
class Dog:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    def bark(self):
        print("bark bark!")
    def setfriend(self, friend):
        self.friend = friend
        friend.friend = self

#Object: e.g. Lacey
Lacey = Dog("Lacey", 2)

#Attribute: e.g. Name and age.
#You add attributes to a class (when creating the object)

#Method : e.g. bark or setfriend
#Function that belongs to an object. You define methods within a class. Call them like this:
Lacey.bark()

#Function:
#A function is a method that is not tied to an object.
def sum(num1, num2):
   return (num1 + num2)

#To call it:
sum(5,6)

#use dir on a function to see all attributes and methods available:
print (dir(variable))

#Use help to find more info on each function:
print (help(str.capitalize))

#Argument: e.g. friends name.
#Pass argument to the method. Put the argument value in brackets (multiple arguments are comma separated)
Lacey.friend(Lilly)

#You can have flexible parameters and pass arguments on the fly with * and ** (positional and key word arguments respectively):
def function_1 (*args, **kwargs):
    print (args)
    print (kwargs)

#and create tuples and dictionaries when calling the function:
function_1('tuple val_1', 'tuple val_2',on_the_fly_param_1='dict val_1', on_the_fly_param_2='dict val 2')

#or pass in ready made tuples and dictionary:
function_1(*tuple_1, **dict_1)