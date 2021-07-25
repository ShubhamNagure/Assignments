# 16.	Write a program to accept the positive integer n 
# from the user and print counting of numbers which are 
# not prime from 1 to n.


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

def countNonPrime(upper):
    lower = 1
    nonPrime=[0, 1]
    primeList=[]
    for num in range(lower,upper + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:
                    nonPrime.append(num)  
                    break  
            else:
                primeList.append(num)  
                # print(num)
    print(len(nonPrime))
if __name__ == "__main__":
    num=positiveIntegerOnly()
    countNonPrime(num)