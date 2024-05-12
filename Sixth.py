#TODO: Function & Recursion


'''Function is block of statements that perform specific task
    Basic syntax
    Def fun_name(param1,param2,......):
        #some work
        return val
    
    fun_name(param1,param2,.....) #function call

'''
# def cal_sum(a,b):
#     sum = a+b
#     print(a+b)

# cal_sum(1,2)
# cal_sum(6,9)
# cal_sum(7,8)

def cal_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)

a = int(input("Enter first Number"))
b = int(input("Enter second Number"))
c = int(input("Enter third Number"))

cal_avg(a,b,c)