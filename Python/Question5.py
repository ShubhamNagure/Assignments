# 5.	Find the Factorial of the given number
def factorial(n):
    factorial = 1  
    i = 1  
    if n < 0:    
        print(" Not defined")    
        exit()
    elif n == 0:    
        return factorial
    while i <=n:
        factorial = factorial* i
        i +=1
    return factorial

if __name__ == "__main__":
    n=input('Enter a number:')
    m=factorial(int(n))
    print(m)