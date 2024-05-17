import random
student = [1,2,3,4,5,6,7,8,9,10,1,4,9,]

finalList = set()
list = set()
allotList = {}
# def sort():
i=0
while i<len(student):
    finalList.add(student[i])
    i+=1
    # return finalList
print(finalList)
mainList = list.union(finalList)
print(mainList)
# sort()
def allot():
    a = 0
    while a<len(finalList):
        stu = random.sample(list(mainList))
        # finalList.remove(stu)
        roll = 234518990 + a    
        allotList.update({stu : roll})
        a+=1
    print(allotList)

allot()
