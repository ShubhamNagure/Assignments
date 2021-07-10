""" 12.	Find the length of longest word from the set of words
  entered by the user"""


def findMaxLen(mylist):
    lenList= []
    for i in mylist:
        lenList.append(len(i))
    
    lenList.sort()

    print("Largest element is:", lenList[-1])
        



if __name__ == "__main__":
    statement=input('Enter statement :')
    mylist=[]
    mylist=statement.split(" ")
    print(mylist)
    findMaxLen(mylist)