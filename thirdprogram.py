#first, we want to get all inputs from the user

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: " )

#this int() function will convert the string input into a integer
birth_year = int (input("Enter your birth year: "))

age = 2024 - birth_year

message = f"Hello {first_name} {last_name}.\nyou are {age} years old"
print(message)

if age>= 19:
    print("You are old enough to drink!")
else: 
    print("Sorry! You are not old enough to drink")

