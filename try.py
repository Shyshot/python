# applicants ={1,2,3,4,7,}
# roll =[]

# def allot():
#      while i<applicants.len():
#            roll[i] = 1253411+i
  
class first:
      value1= "first"
      def tell(self):
            print("I am",self.value1)

class second(first):
      value2 ="Second"
class Third(second):
      value3 = "Third"
      def tell2(self):
            print("I am ",self.value3)
      
num = Third()

num.tell()