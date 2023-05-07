#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password=[]
for letter in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password+=random_char

for number in range(1,nr_numbers+1):
    random_num=random.choice(numbers)
    password+=random_num
  
for symbol in range(1,nr_symbols):
    random_symbol=random.choice(symbols)
    password+=random_symbol
    
for shuffle in password:
    random.shuffle(password)
   
new_password=""
for last_passowrd in password:
  new_password+=last_passowrd 
print(f"Your Password is :{new_password}")   




  