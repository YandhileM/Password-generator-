import random
import string

#function to generate password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits +string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#promt to user
sizeOfPassword = int(input("Enter length of password you want."))

password = generate_password(sizeOfPassword)


print("Your generated password:", password)