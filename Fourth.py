#TODO: Dictionary & set



# info = {
#     "key" : "value",        #This is Basically object from javascript but are muttable and can store both tupples and lists
#     "name":"Piyush",
#     "learning":"Python",
#     "age":"69",
#     "idAdult":True,
#     "Language":["python","javascript","CSS","HTML"],
#     "topics":("dict","set")
# }
# print(info)             #The Above  Dict Can be Accessed using this Syntax
# print(info["key"])          #Value of key can be used by following syntax
# print(type(info))

# info["key"]="Piyush" #A specific key can be changed in the following form
# print(info["key"]);

# null_dict = {} #A Null dict can be created and later be filled by the following syntax
# null_dict["name"]="Piyush";

# print(null_dict)


#FIXME: NESTED DICT


# student = {
#     "name":"Piyush Singh",
#     "subject":{
#         "phy":67,
#         "chem":99,
#         "maths":69
#     }

# }
# print(student)
# print(student["subject"])
# print(student["subject"]["chem"])           #This Way the Value inside the nest Can be acccessed


 #FIXME: METHODS 

# print(student.keys())          #returns all keys
# print(student.values())         #returns all values
# print(student.items())         #returns all (key,val) pairs as tuples
# print(student.get("name"))         #returns the key according to the value
# student.update({"city":"Mumbai"})            #inserts the specified items to the dictionart
# print(student)


#FIXME:  Set

'''Set is the Collection of the unordered items
   Each Element in the et must be unique & immutable'''

collection = {1,2,3,4,"Hello","World",2,5}          #Set ignores Duplicate Values While Giving the output & Gives the output in a completely random order
# print(collection)
# print(len(collection))          #Even the Length method ignores the Duplicate values in the sets


# null_set = {} This Creates a Empty DICT not a Empty set thus a empty set is formes as
# null_set = set()
# print(type(null_set))

#FIXME: Set Methods


# collection.add(6)          #Adds An element
# collection.remove(2)            #Removes the element
# # collection.clear()          #empties the set
# print(collection.pop())           #removes random values
# print(collection)

set1 = {1,2,4,5,7}
set2 = {1,2,8,9,8,7}

# set3 = set1.union(set2)            #Combines both set values& returns new
# print(set3)
   
# set4 = set1.intersection(set2)          #combines common values &returns new
# print(set4)
# set5 = set2.intersection(set1)

# if(set4 == set5):
#     print("Interscetion same")
# else:
#     print("interscetion unique")
