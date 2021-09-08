# Write a Python program
#  to match a string that contains only upper and lowercase letters, numbers, and underscores
#  to Find Sum of Natural Numbers Using Recursion


import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))

"""
B. to Find Sum of Natural Numbers Using Recursion
"""

# Python code to find sum
# of natural numbers upto
# n using recursion

# Returns sum of first
# n natural numbers
def recurSum(n):
	if n <= 1:
		return n
	return n + recurSum(n - 1)

# Driver code
n = 5
print(recurSum(n))
