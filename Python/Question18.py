# 18.	Write a code to accept the string of length 10  from the
#  user and print True if string has any character occurring 5 
# times consecutively in it, otherwise print False

def strLenTenOnly():
    goodinput = False
    while not goodinput:
        inpStr = input('Enter a String: ')
        if len(inpStr) == 10:
            goodinput = True
            return inpStr
        else:
            print("String length should be 10 char. Try again: ")

def checkOccrance(inpStr):
    """Check Occurence of 5 times"""
    for i in inpStr:
        ctr=0
        for j in inpStr:
            if i==j:
                ctr+=1
                if ctr ==5:
                    return True

if __name__ == "__main__":
    inpStr=strLenTenOnly()
    flag=checkOccrance(inpStr)
    print(flag)