#TODO: File Input Output


from dataclasses import dataclass
from distutils.command.sdist import sdist
from fileinput import close

# f = open("demmo.txt","r")           #The multiple methods can be used simaltaneously by writing them together

 #FIXME: File Methods
'''
    character              Meaning
      
      'r'                   open for reading(default)
      'w'                   open for writing,truncating the file,this completely rewrites the file
      'x'                   create a new file and open it for writing
      'a'                   open for writing, appending to the end of the filr if it exists,this does not rewrites the file completely
      'b'                   binary mode fot png,mp4,etc.
      't'                   text mode(default)
      '+'                   open a disk file for updating (reading and writing)  

'''

# data = f.read()        #The argument passed in the fucntion is about the  number of character neaded to read from the file   
# print(data)             
# print(type(data))
# f.close()

# line1 = f.readline()        #This method reads one at a time from the file
# print(line1)

# line2 = f.readline()        #If the line is already read then the metod reads another line simalarly if the entire file is alreadt read then the method will not read

# print(line2)

# f = open("demmo.txt","w")     #Now it is open with the method to overwrite.

# f.write("Iske baad bhi kuch khass hua nahi")      #This will be owerwrtied in the file

# f.close


# f = open("demmo.txt","a")       #Now it is open with the method to append

# f.write("\n Iske baad bhi kuch khass hua nahi")       #This will be added in the end of file

# f.close()

# f = open("newDemo.txt","w")         If a file opened with write or append method it creates a new file 

#FIXME: with syntax

'''This is a modular style or block style of writing file input and output'''

# with open("demmo.txt","r") as f:
#   data = f.read()
#   print(data)

# import os

# os.remove("demmo.txt")

#FIXME: Practice Questions

# f = open("practice.txt","r")

# f.write("Hii Everyone")
# f.write("\nwe are learing fie I/O")
# f.write("\nusing python")
# f.write("\nI like programming in python")
# data=f.read()
# newData = data.replace("python","Java")
# f.close()

# r = open("practice.txt","w")
# r.write(newData)

# data = f.read()

# if(data.find("learning") != -1):
#   print("Mil gaya")
# else:
#    print("Naah nahi hai")
# word = "learning"
# word2 = "Java"
# def CheckForWord(W):
#   f = open("practice.txt","r")
#   data = True
#   lineNo = 1
#   while data:
#     data = f.readline()
#     if(data.find(W) != -1):
#       print("The Word is found in line No",lineNo)
#     lineNo +=1
# CheckForWord(word2)