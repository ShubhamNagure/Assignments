# 17.	Write a program to accept the two +ve integers start and stop 
# where 0<start<stop<=100. print all numbers from start to stop both
# inclusive If the number is divisible by 3 print Divisible by 3 at 
# the place of number. If the number is divisible by 5 print Divisible
# by 5 at the place of number. If the number is divisible by 10 print 
# Divisible by 10 at the place of number. If the number is divisible by
#  any of two from 3, 5 and 10 , print nothing, just skip. If the number
#  is divisible by all ( 3 , 5 and 10) , stop printing the number. If the
#  number is not divisible by any of (3 , 5 and 10) ,  just print the 
# number as it is.

def checkNum(startNum,stopNum):
    """"accept and check the two +ve integers start and stop"""
    #corner cases
    if startNum < 0 :
        print("Startnum is not a valid interger")
        exit()
    if stopNum < 0:
        print("Stop number is not valid integer")
        exit()
    if startNum > stopNum:
        print("Please enter a valid range")
        exit()

    numList=[]
    for i in range(startNum,stopNum+1):
        numList.append(i)
    return numList

def checkDivByThree(numList):
    """print Divisible by 3 at the place of number"""
    for i in numList:
        if (i%3 ==0):
            print(i , "Divisible by 3")

def checkDivByFive(numList):
    """ print Divisibleby 5 at the place of number"""
    divBy5list= []
    for i in numList:
        if (i%5 ==0):
            print(i , "Divisible by 5")
            divBy5list.append(i)
    return divBy5list

def checkDivByTen(numList):
    """print Divisible by 10 at the place of number"""
    divBy10List = []
    for i in numList:
        if (i%10 == 0):
            print(i , "Divisible by 10")
            divBy10List.append(i)


def checkOnlyTwoDiv(numList):
    """If the number is divisible by any of two from 
    3, 5 and 10 , print nothing """
    flag =False
    for i in numList:
        if ((i%3 == 0) and (i%5 == 0)):
            flag =True
        if(i%5 == 0) & (i%10 ==0):
            flag =True
    return flag

def checkDivByAll(numList):
    """"If div by 3,5,10 stop printing"""
    for i in numList:
        if (i%3 == 0 and i%5 == 0 and i%10 == 0):
            print(i,"Exit Because this num is divisible by all 3,5,10")
            exit()


def notDivAtAll(numList):
    for i in numList:
        if (i%3 != 0 and i%5 != 0 and i%10 != 0):
            print(i)

# Driver code
if __name__ == "__main__" :
    startNum =int(input("Enter A Start number :"))
    stopNum =int(input("Enter A Stop number :"))

    listOfNums= []
    #implementation:
    listOfNums = checkNum(startNum,stopNum)
    """GENERAL: this methods are `loop, check and print`"""
    checkDivByThree(listOfNums)
    print('#' * 100)

    checkDivByFive(listOfNums)
    print('#' * 100)

    checkDivByTen(listOfNums)
    print('#' * 100)

    #
    checkOnlyTwoDiv(listOfNums)
    print('#' * 100)
    #
    checkDivByAll(listOfNums)
    print('#' * 100)