#TODO: OOPS (Class,Object,Constructor,Attributes,Methods,Abstraction, Encapsulation)

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
# class Student:
#     college_Name = "BHU"
#     name = "Annnoynous"
    #Default Constructor
    # def __init__(self) :
    #     pass
    #Paramerterized Constructor
    # def __init__(self,name,marks):   The Can be named Whatever we need, but generally for easier Communication it is kept as self and is used to get variables in the class
    #     self.name =  name
    #     self.marks = marks

#Creating Object
# s1 = Student("Karan",88)
# s2 = Student("Arjun",98)

# print(s1.name ,s1.college_Name)
# print(s2.name ,s2.college_Name)


#The self parameter is a reference to the current insatance of the class, and is used to access variables that belongs to the class
#If a constructor has both Default and parameterized construtor then the constructor matching the way the class is called will be Used, Generally Multiple Constructor is not created in a classs



#FIXME: Class & Instance(Object) Attributes


"""Class Attributes are Attributes which are common For all the object For Example: In above class all the objects will have same collge_name Attributes
   Instance(object) Attributes are attributes which Changes from object to object For Example : In above cass all the objects will have the name and marks Attributes as defined
"""
#If Class and object(Instance) both have same Attributes then the Object Attribute will have greater priority
#This is not usual done but created sometimes to aviod Errors

#FIXME: Methods
"""Methods are functions that belong to object
"""
# Creating Method

# class Student:
#     def __init__(self,fullname):
#         self.name = fullname
    
#     def hello(self):
#         print("hello",self.name) #Methods also have self as there First Parameter
    
# Creating Object

# s1 = Student("Karan")
# s1.hello()

#Pratice

# class student:
#     def __init__(self,English,Maths,Science):
#         self.m1 = English
#         self.m2  = Maths
#         self.m3 = Science
#     def calcAvg(self):
#         total = self.m1  + self.m2 + self.m3
#         avg = total/3
#         return avg
    
# m1 = int(input("Enter Marks for English\n"))
# m2 = int(input("Enter Marks for Maths\n"))
# m3 = int(input("Enter Marks for Science\n"))


# s1 = student(m1,m2,m3)
# print("The Average score is",s1.calcAvg())

#FIXME: Static Methods

""" Methods That don't use the self parameter (work at class level)

"""
# class Student:
#     @staticmethod           #decorator
#     def college():
#         print("ABC College")

# s1 = Student()
# s1.college()
"""Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it"""

#FIXME: Abstraction
"""Hiding the implementation details of a class and only showing the essential features to the user."""

# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk =False
#         self.clutch = False
#     def start(self):
#         self.clutch = False
#         self.acc = True
#         self.brk = False
#         print("Car has Moved") 

# porsche = car()
# porsche.start()

#FIXME: Encapsulation

# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk =False
#         self.clutch = False
#     def start(self):
#         self.clutch = False
#         self.acc = True
#         self.brk = False
#         print("Car has Moved") 

#Its all about Collecting all the required variable and proccess in a single block making it  storage friendly and easier ot execute

"""Wrapping data and functions into a single unit(object)"""

#Practice

class Account :
    def __init__(self,balance,account_no):
        self.balance = balance 
        self.account_no = account_no
    def debit(self,amm):
        self.balance =self.balance - amm
        print("Ammount",amm,"was Debited from",self.account_no)
        print("Remaining Balance",self.balance)
    def credit(self,amm):
        self.balance += amm
        print("Ammount",amm,"was Credited from",self.account_no)
        print("Remaining Balance",self.balance)

p1 = Account(700000,85475124511)
p1.debit(7500)
p1.credit(70000)