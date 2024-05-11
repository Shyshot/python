#TODO: Strings and Conditionals



# str1 = "Piyush"
# str2 = "coder"
# str3 = "Python Begins Here"
# # print(str1[0])
# print(str3.find("Here"))
# print(str3.replace("Python","Javascript"))
# print(str2.capitalize())
# print(str3.count("h"))

# Name = input("Enter Your Name:\n")
# str1 = "Hii $Iam $ sign $ $ $$"
# count =  len(Name)
# print(str1.count("$"))
# print("You Name has ", count , " Letters")




# age =int( input("Enter Your Age \n"))
# print("Since your age is ", age," ")
# if(age >= 18):
#     print("You are Eligible For Drivers License")

# elif(age >=16):
#     print("Your are Eligible for Learner License")
# else:
#     print("You are not Eligible for License")


a = int(input("Enter 1st Number\n"))
b = int(input("Enter 2nd Number\n"))
c = int(input("Enter 3rd Number\n"))
d = int(input("Enter 4th Number\n"))

if(a>b and a>c and a>d):
    print("A is Largest")
elif( b>c and b>d):
    print("B is Largest")
elif(c>d):
    print("C is Largest")
else:
    print("D is largest")