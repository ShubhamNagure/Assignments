# 2. Find whether the given number ends with 0 or 5 or any other number

def divBy5or10(n):
    if n%5 ==0 and n%10 ==0 :
        print('0')
    elif n%5 ==0 and n%10 !=0:
        print('5')
    else:
        print('Other')
    

if __name__ == "__main__":
    n=input('Enter a number:')
    divBy5or10(int(n))
