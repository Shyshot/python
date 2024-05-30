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
    college_Name = "BHU"
    name = "Annnoynous"
    #Default Constructor
    # def __init__(self) :
    #     pass
    #Paramerterized Constructor
    def __init__(self,name,marks):   #The Can be named Whatever we need, but generally for easier Communication it is kept as self and is used to get variables in the class 
        self.name =  name
        self.marks = marks

#Creating Object
s1 = Student("Karan",88)
s2 = Student("Arjun",98)

print(s1.name ,s1.college_Name)
print(s2.name ,s2.college_Name)


#The self parameter is a reference to the current insatance of the class, and is used to access variables that belongs to the class
#If a constructor has both Default and parameterized construtor then the constructor matching the way the class is called will be Used, Generally Multiple Constructor is not created in a classs



#FIXME: Class & Instance(Object) Attributes


"""Class Attributes are Attributes which are common For all the object For Example: In above class all the objects will have same collge_name Attributes
   Instance(object) Attributes are attributes which Changes from object to object For Example : In above cass all the objects will have the name and marks Attributes as defined
"""
#If Class and object(Instance) both have same Attributes then the Object Attribute will have greater priority
#This is not usual done but created sometimes to aviod Errors
