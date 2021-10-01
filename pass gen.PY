import string
import random
length = int(input("Enter password lenght\n"))#command generated to input length for password

s1= string.printable
str =[]
str.extend(list(s1))
print("Your password is")
print("".join(random.sample(str,length)))
