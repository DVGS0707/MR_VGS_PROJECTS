import string
import random
leng = int(input("Enter password lenght\n"))#command generated to input length for password

s1= string.printable
s =[]
s.extend(list(s1))
print("Your password is")
print("".join(random.sample(s,leng)))
