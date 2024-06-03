#TODO: OPPS  ()

#FIXME: del Keyword

"""Used to delete Object properties or object itself"""

# class Student:
#     def __init__(self,name):
#         self.name = name
    
# s1 = Student("Piyush")
# print(s1)
# del s1 
# print(s1)

#FIXME: Private(like) attributes & Methods

"""Conceptual Implementation in python 

    Private attributes & methods are meant to be used only within the class and are not accessible from outside the class
    This can be but by adding two __ before the name of the attribute
"""
# class Account:
#     def __init__(self, accNo,accPass):
#         self.accNo = accNo
#         self.__accPass = accPass

#     def resetPass(self):
#         print(self.__accPass)       #Here the value will be printed as the Method belog to the same class and the attribute has private Scope
# acc1 = Account(8475221,"Piyush@123")
# acc1.resetPass()
# print(acc1.__accPass)  #Here The Value well not be printed due to the private scope of the attribute.

"""Similarly a method can be created Having two __ before the name , this kind of methods are created to be used by other methods in the same function"""

#FIXME: Inheritance

"""When one class(class/derived) derives the properties & methods of another class (parent/base)"""
#TODO: Single Inheritence
# class Car:
#     color = "black"
#     def start(self):
#         print("Car has Started...")
#     def stop(self):
#         print("Car has Stopped...")
    
# class Toyota(Car):              #Inheritence can be established by add a bracket at the end of the child class name and mentioning the parent class
#     def __init__(self,name):
#         self.name = name
    
# car1 = Toyota("Fotuner")
# car2 = Toyota("prius")

# print(car1.name)        #This is the Attribute that car1 had
# print(car1.color)       #These are the Attribute that car1 Inherited from the class car
# car1.start() 


#TODO: Multi - level Inheritence

# from typing import Type


# class Car:
#     def start(self):
#         print("Car has Started...")
#     def stop(self):
#         print("Car has Stopped...")
    
# class Toyota(Car):    
#     brand = "Toyota"          
#     def __init__(self):
#         self.Brand = "Toyota"   
# class Fortuner(Toyota):
#     def __init__(self,type):
#         self.type = type

# car1 = Fortuner("Diesel")

# print(car1.brand)   
# # print(car1.Brand)   #Inheritence does not inherit the Attributes or Methods Defined in Constructor
# car1.start()


#TODO: Multiple Inheritence

# class A :
#     varA = "Welcome to class A"

# class B :
#     varB = "Welcome to class B"

# class C (A,B):
#     varC ="Welcome to class C"

# s1 = C()
# print(s1.varA) 
# print(s1.varB) 
# print(s1.varC) 




#FIXME: Super Method

"""super() method is used to access methods of the parent class"""

class Car:
    def __init__(self,type):
        self.type = type
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car has stopped")
    
class Toyota(Car):
    def __init__(self,brand,type):
        self.brand = brand


car1 = Toyota("Pirus")

print(car1.type)



