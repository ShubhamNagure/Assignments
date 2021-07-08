# 7.	Reverse the Digits in the given number

def easyRev(n):
    """Easy Method"""
    print(n[::-1])

def revDigits(n):
    """With While loop"""
    rev=0
    flag=True
    while n > 0:
        a = n % 10
        rev=rev*10 + a
        n=n//10
    print(rev)


if __name__ == "__main__":
    n=input('Enter a number:')
    revDigits(int(n))
    # easyRev(n)