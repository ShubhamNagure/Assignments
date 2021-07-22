"""FIND PALINDROME WITH LIST"""

def addList(n):
    templist =[]

    for i in n:
        templist.append(i)

    return templist

def reverseList(templist):
    revlist=[]

    revlist=templist[::-1]

    return revlist


def checkPalindrome(templist,revlist):
    
    if templist == revlist:
        print("Palindrome")
    else:
        print("nothing")

if __name__ == "__main__":
    n=input("Enter a number:" )
    #n=1234321
    ls=addList(n)
    revlist=reverseList(ls)

    print("ls is :", ls)
    print("revesres list is: ", revlist)

    checkPalindrome(ls,revlist)
