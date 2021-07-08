# 6.	Find the number of digits in the given number

def easyLen(n):
    """Easy Method"""
    print(len(n))

def lenOfDigits(n):
    """With While loop"""
    i = 0
    flag=True
    while n != 0:
        n = n//10
        i +=1
    print(i)


if __name__ == "__main__":
    n=input('Enter a number:')
    lenOfDigits(int(n))
    # easyLen(int(n))