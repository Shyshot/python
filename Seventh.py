#TODO: File Input Output


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


