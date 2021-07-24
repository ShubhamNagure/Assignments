#13.Write a Python program to construct the following pattern,
#  using a nested for loop
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * *       
* * * 
* * 
*
"""

def upwordPyramid():
    # number of rows
    rows = 5
    for i in range(0, rows):
        # nested loop for each column
        for j in range(0, i + 1):
            # print star
            print("*", end=' ')
        # new line after each row
        print("\r")
def downwordPyramid():
    rows = 4
    for i in range(rows + 1, 0, -1):
        # nested reverse loop
        for j in range(0, i - 1):
            # display star
            print("*", end=' ')
        print(" ")



if __name__ == "__main__":
    upwordPyramid()
    downwordPyramid()