import random

#Below we have the list of letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!' '@', '#', '$', '%', '^', '&', '*', '(', ')', '\\',]

#Welcome statement as the begining of the program
print("Welcome to the password generator")

# I get 3 inputs from the user 
num_letters = int(input("How many letters do you want in your password?  "))
num_numbers = int(input("How many numbers do you wnat in your password?  "))
num_symbols = int(input("How many symbols do you wnat in your password?  "))

# I have a password list and a password string. We do not need the string for now until the end
password = [] 
password_string = ""

""" I get a random letter, numbers, or a symbol 
    (for as many as the user wanted and specified in the inputs) and I add it to the list
"""
for item in range(num_letters):
    password.append(random.choice(letters))

for item in range(num_numbers):
    password.append(random.choice(numbers))

for item in range(num_symbols):
    password.append(random.choice(symbols))

# Then I shuffle the list
random.shuffle(password)

# Then I add each of the letter in the list to an empty string so the user can see it as a string
for items in password:
    password_string += items

print(f" Your password is : {password_string} ")



