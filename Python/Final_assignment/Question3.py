# Write a Python program for email validation.

import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def check(email):   
  
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")   
      
if __name__ == '__main__' :   
      
    email = input("Enter a Email ID to validate: --> ") 
    check(email)   
  