# 14.	First n even numbers in reverse order

def findEvenNum(n):
    myevenList=[]
    for i in range(0,n):
        if i%2 ==0:
            myevenList.append(i)
    
    return myevenList

def printReverse(ls):
    revlist=ls[::-1]
    print(revlist)

if __name__ == "__main__":
    n=int(input("Enter the number :"))
    ls=findEvenNum(n)
    printReverse(ls)