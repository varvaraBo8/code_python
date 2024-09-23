#password generator

#module import
import random

# ASCII table decimal to characters
lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58,65)) + list(range(91,97)) + list(range(123,127))

#make an empty password
password = ""
options = lowercase.copy()

#this will ask the user the size of the password
size = int(input("Enter the size of the password"))

#This will ask the user for the password requirements 
has_upper = input ("Include uppercase letter? (Y/N): ")
has_digit = input("Include numbers? (Y/N): ")
has_special = input("Include specical charecters? (Y/N): ")

if has_upper in {'Y', 'y'}:
       options.extend(uppercase)
if has_digit in{'Y', 'y'}:
       options.extend(digits)
if has_special in {'Y', 'y'}:
       options.extend(special)

while len(password) < size:
    random_char = chr(random.choice(options))
    password += random_char

print(f"the randomly generated password is: {password}")