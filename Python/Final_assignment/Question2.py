# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

# Password validation in Python
# using naive method

# Function to validate the password
def password_check(passwd):
	
	SpecialSym =['$', '#', '@']
	val = True
	
	if len(passwd) < 6:
		print('length should be at least 6')
		val = False
		
	if len(passwd) > 16:
		print('length should be not be greater than 16')
		val = False
		
	if not any(char.isdigit() for char in passwd):
		print('Password should have at least one numeral')
		val = False
		
	if not any(char.isupper() for char in passwd):
		print('Password should have at least one uppercase letter')
		val = False
		
	if not any(char.islower() for char in passwd):
		print('Password should have at least one lowercase letter')
		val = False
		
	if not any(char in SpecialSym for char in passwd):
		print('Password should have at least one of the symbols $@#')
		val = False
	if val:
		return val

# Main method
def main():
	passwd=input("Enter A password to validate : -->  ")
	
	if (password_check(passwd)):
		print("Password is valid")
	else:
		print("Invalid Password !!")
		
# Driver Code		
if __name__ == '__main__':
	main()
