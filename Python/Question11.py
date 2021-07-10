"""11.	Find the day wise total rainfall for entered duration of time
 e.g. week, month, etc."""

__author__ = "Shubham Nagure"


"""
`OUTPUT:`
PS C:\Users\shubh\Personale\ASSIGNEMENT\Assignment\Assignments\Python> python .\Question11.py
Enter the duration :7
Enter a number :10
Enter a number :15
Enter a number :19
Enter a number :5
Enter a number :-1
49
Enter a number :12
Enter a number :13
Enter a number :31
Enter a number :-1
56
Enter a number :57
Enter a number :32
Enter a number :85
Enter a number :47
Enter a number :82
Enter a number :-1
303
Enter a number :2
Enter a number :5
Enter a number :8
Enter a number :2
Enter a number :4
Enter a number :8
Enter a number :8
Enter a number :2
Enter a number :-1
39
Enter a number :-1
0
Enter a number :21
Enter a number :73
Enter a number :90
Enter a number :3
Enter a number :7
Enter a number :-1
194
Enter a number :30
Enter a number :17
Enter a number :40
Enter a number :10
Enter a number :2
Enter a number :-1
99

"""

def createList(dur): 
    m=0
    while m != dur:
        n=1
        nums=[]
        while n != -1:
            n=int(input('Enter a number :'))
            if n == -1:
                break
            else:
                nums.append(n)
        m+=1
        dayWiseTotalRainfall(nums)


def dayWiseTotalRainfall(nums):
    sum=0

    for i in nums:
        sum=sum+i

    if sum <= 0:
        print('0')
    else:
        print(sum)

if __name__ == "__main__":

    dur=int(input('Enter the duration :'))
    listOfRainfall=[]
    listOfRainfall=createList(dur)

