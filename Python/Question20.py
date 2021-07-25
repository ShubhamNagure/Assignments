# 20.	Write a python program that repeatedly prompts a user for 
# integer numbers until the user enters 'Done'. Once 'Done' is entered,
#  print out the number of positive, number of negative, number of zeros,
#  sum & average of positive digits and sum & average of negative digits 
# entered by the user. If the user enters anything other than a valid
#  number, catch it with a try/except and put out an appropriate message 
# and ignore the entered character


def integerNums():
    redFlag =False
    inpList=[]
    while not redFlag:
        try:
            number = input('Enter a integer: ')
            if number.lower() == 'done':
                redFlag= True
                break
            else:
                inpList.append(int(number))
        except ValueError:
            print("that's not an integer. Try again: ")
    return inpList

def numOfPositive(inpls):
    postiveList=[]
    for i in inpls:
        if i > 0 :
            postiveList.append(i)
    return postiveList

def numOfNegetive(inpls):
    negetiveList=[]
    for i in inpls:
        if i < 0 :
            negetiveList.append(i)
    return negetiveList

def numOfZeros(inpls):
    zerosList=[]
    for i in inpls:
        if i ==0:
            zerosList.append(i)
    return zerosList

def sumAndAvgOfPos(posList):
    sum=0
    avg = 0
    for i in posList:
        sum=sum+i
    avg=sum/len(posList)

    return avg


def sumAndAvgOfNeg(negList):
    sum =0
    avg=0
    for i in negList:
        sum=sum+i
    avg= sum/len(negList)
    return avg

if __name__ == "__main__":
    inpls=integerNums()
    posList=numOfPositive(inpls)
    print("Number of positive Integers: ", len(posList))

    negList=numOfNegetive(inpls)
    print("Number of Negetive Integers: ",len(negList) )

    zeroList=numOfZeros(inpls)
    print("Number of zeros: ",len(zeroList) )

    avgPos=sumAndAvgOfPos(posList)
    print("Average of positive :", int(avgPos))

    avgNeg=sumAndAvgOfNeg(negList)
    print("Average of negeive :", int(avgNeg))