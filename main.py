import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
for i in range(1, nr_letters + nr_symbols + nr_numbers + 1):
    if i <= nr_letters:
        password.append(random.choice(letters))
    elif i <= nr_letters + nr_symbols:
        password.append(random.choice(symbols))
    elif i < nr_letters + nr_symbols + nr_numbers + 1:
        password.append(random.choice(numbers))
print(password)

random.shuffle(password)
print(password)

your_password = ''
for symbol in password:
    your_password += symbol

print(f"Your password is: {your_password}")