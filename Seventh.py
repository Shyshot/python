from distutils.command.sdist import sdist
from fileinput import close

f = open("demmo.txt","r")           #The multiple methods can be used simaltaneously by writing them together

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

# data = f.read(5)        #The argument passed in the fucntion is about the  number of character neaded to read from the file   
# print(data)             
# print(type(data))
# f.close()

line1 = f.readline()        #This method reads one at a time from the file
print(line1)

line2 = f.readline()
print(line2)