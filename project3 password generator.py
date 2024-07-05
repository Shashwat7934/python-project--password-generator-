import random      #importing random module for random combination of password
import string      #importing string module for entering types of character in the password
print("welcome to our random password generator")       #welcoming the user
length = int(input("enter the length of the password you want to enter:"))      #entering the length of password 

lowerdata = string.ascii_lowercase         #using the string methods to place lowercase ,uppercase,digits and special combination in the password
upperdata = string.ascii_uppercase
digit = string.digits
symbol = string.punctuation

combine = lowerdata+upperdata+digit+symbol   #concatenating the all comination in the varaibe

x = random.sample(combine,length)       #using random.sample  method to generate random combination of the passwords
password= "".join(x)
print(password)                     #print the require password o the screen



