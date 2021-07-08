# 1. Find whether the given number is even or odd

def evenOrOdd(n):
    if n%2 ==0 :
        print('Even')
    elif n%2 !=0:
        print('Odd')
    

if __name__ == "__main__":
    n=input('Enter a number:')
    evenOrOdd(int(n))
