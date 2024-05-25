#TODO: OOPS

'''To map with real world scennarios, we started, we started using objects in code
    This is called object oriented programming
'''
#FIXME: Class & Object in Python
#Class is a blueprint for creating objects.

# class Student:
#     name = "karan Kumar"        #TODO:This is a class

# s1 = Student                     #TODO: This is a Object
# print(s1)

# class car:
#     color = "Blue"
#     brand = "Porsche"

# car1 = car()
# print(car1.color)

#FIXME: __init__ Function

'''Constructor
    All classes have a function called __init__(), which is always executed when the class is being initiated
'''
#Creating class
class Student:
    def __init__(self,fullname):
        self.name =  fullname

#Creating Object
s1 = Student("Karan")
print(s1.name)

#The self parameter is a reference to the current insatance of the class, and is used to access variables that belongs to the class