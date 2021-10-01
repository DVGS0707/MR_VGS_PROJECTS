import string
import random
length = int(input("Enter password your length\n"))#command generated to input length for password
str_pass= string.printable #its function is to print the random combination of string integers and special characters.
str =[]
str.extend(list(str_pass))
print("Your password is:")
print("".join(random.sample(str,length)))
