#TODO:Lists & Tuples



# marks = [87, 64,78.3,98,69]
# print(marks[1])
# print(marks[0])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# marks.append(64)       #Adds one element at the end
# marks.sort()       #sorts in ascending order
# marks.sort(reverse=True)       #sorts in Descending order
# marks.reverse()       #reverses list
# marks.insert(2,76)       #insert element at index
# marks.remove(87)       #Removes first occurencce of elements
# marks.pop(2)       #removes Element at idx
# print(marks)

'''This also Works on Strings based on Alphabetical order'''

'''Tuples is a built-in data type that lets us create Immutable sequences of values'''

# tup = (1,2,4,1,5,7,9)
# print(tup)
# print(tup.index(1))       #returns index of first occurrence
# print(tup.count(1))       #counts total occurences


movie1 = input("Enter 1st Movie Name\n")
movie2 = input("Enter 2nd Movie Name\n")
movie3 = input("Enter 3rd Movie Name\n")            
# list.insert(1,movie2)
# list.insert(2,movie3)                              
list = [movie1,movie2,movie3]

list.sort()
print(list)