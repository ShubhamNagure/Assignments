# 15.	Write a program to accept a positive integer n from the user
#  and print the average of all numbers factorial from 1 to n


def positiveIntegerOnly():
    goodinput = False
    while not goodinput:
        try:
            number = int(input('Enter a number: '))
            if number > 0:
                goodinput = True
                return number
            else:
                print("that's not a positive number. Try again: ")
        except ValueError:
            print("that's not an integer. Try again: ")

def avgOfFact(n):
    myint=[]
    for i in range(0,n):
        myint.append(i)
    
    sum =0
    avg=0
    l= len(myint)-1
    for j in myint:
        sum=sum+j
    
    avg=sum/l
    print("Avg of all numbers factorial from 1 to ",n )

    
    

if __name__ == "__main__":
    n=positiveIntegerOnly()
    avg=avgOfFact(n)
