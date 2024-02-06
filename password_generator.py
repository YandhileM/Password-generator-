import random
import string

#function to generate password
def generate_password(length=12, uppercase=True,lowercase=True, digits=True, special=True):
    characters =''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits 
    if special:
        characters += string.punctuation
    if not characters:
        print("Error: None selected.")
        return None
    
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#promt to user
sizeOfPassword = int(input("Enter length of password you want."))
uppercase = input("Do you want to include uppercase letters? (Yes/No)").lower() == 'yes'
lowercase = input("Do you want to include lowercase letters? (Yes/No)").lower() == 'yes'
digits = input("Do you want to include intergers? (Yes/No)").lower() == 'yes'
special = input("Do you want to include punctuation marks? (Yes/No)").lower() == 'yes'

password = generate_password(sizeOfPassword, uppercase, lowercase, digits, special)

if password:
    print("Your generated password:", password)