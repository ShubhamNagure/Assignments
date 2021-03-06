"""
A positive integer m can be partitioned as primes if it can be written as p + q where p > 0, q > 0 and both p 
and q are prime numbers. Write a Python function primepartition(m) that takes an integer m as input and returns 
True if m can be partitioned as primes and False otherwise. (If m is not positive, your function should return False.)

"""

def primepartition(m):
    primelist=[]
    if m<0:
        return False
    else:
        for i in range(2,m + 1):
            for p in range(2,i):
                if (i % p) == 0:
                    break
            else:
                primelist.append(i)

        for x in primelist:
            y= m-x
            if y in primelist:
                return True
        return False

print(primepartition(-10))