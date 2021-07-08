# 3. Find the grade of student based on the given marks from 0 to 100.

def studentGrades(n):
    if n >= 90 :
        print('A')
    elif n >=80 and n < 90:
        print('B')
    elif n >=70 and n < 80:
        print('C')
    elif n >=60 and n < 70:
        print('D')  
    elif n < 60:
        print('E')                
    else:
        print('INVALID INPUT')
    

if __name__ == "__main__":
    n=input('Enter a number:')
    studentGrades(int(n))