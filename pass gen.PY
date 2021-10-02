#this is a password generator
import string
import random


# characters to generate password 
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	# length of password input
	length = int(input("Enter password length: "))

	# shuffling the characters
	random.shuffle(characters)
	
	# picking random characters from list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	# shuffling resultant password
	random.shuffle(password)

	# converting the list to string and
	print("".join(password))


## invoking the function
generate_random_password()
