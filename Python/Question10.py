""" 10.	Find the total profit/loss of each trader working in a trading firm.
Information regarding number of traders and number of transaction is 
unknown """

__author__ = "Shubham Nagure"

def createList():
    n=1
    nums=[]
    
    while n != 0:
        n=int(input('Enter a number :'))
        nums.append(n)
    return nums

def profitAndLoss(nums):
    sum=0

    for i in nums:
        sum=sum+i

    if sum <= 0:
        print('0')
    else:
        print(sum)

if __name__ == "__main__":
    traderId=input('Enter Id of Trader :')
    listOfTx=[]
    listOfTx=createList()

    profitAndLoss(listOfTx)

"""
`OUTPUT`

PS C:\Users\shubh\Personale\ASSIGNEMENT\Assignment\Assignments\Python> python .\Question10.py
Enter Id of Trader :SJ_323
Enter a number :3534
Enter a number :56456
Enter a number :-2432
Enter a number :0
57558

"""