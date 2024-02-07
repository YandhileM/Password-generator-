import random
import string
import tkinter as tk
from tkinter import messagebox

#function to generate a random password
def generate_password(sizeOfPassword=12, uppercase=True,lowercase=True, digits=True, special=True):
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
    
    
    password = ''.join(random.choice(characters) for i in range(sizeOfPassword))
    return password

#Function to generate password when button is clicked
def generate_password_click():
    sizeOfPassword =int(size_entry.get())
    uppercase = uppercase_var.get()
    lowercase = lowercase_var.get()
    digits = digits_var.get()
    special = special_var.get()

    password = generate_password(sizeOfPassword, uppercase, lowercase, digits, special)
    if password:
        password_display_label.config(text="Generated password: " +password)

#GUI
root = tk.Tk()
root.title("Password Generator")

sizeOfPassword_label = tk.Label(root, text = "Enter length of password you want:       ")
sizeOfPassword_label.pack(pady=5)

size_entry = tk.Entry(root)
size_entry.pack(pady=5)

#checkbox to include
uppercase_var = tk.BooleanVar()
uppercase_var.set(True)
uppercase_check = tk.Checkbutton(root, text ="Uncheck the checkbox if you do not want to include uppercase letters", variable = uppercase_var)
uppercase_check.pack()

lowercase_var = tk.BooleanVar()
lowercase_var.set(True)
lowercase_check = tk.Checkbutton(root,text = "Uncheck the checkbox if you do not wish to include lowercase letters", variable = lowercase_var)
lowercase_check.pack()

digits_var = tk.BooleanVar()
digits_var.set(True)
digits_check = tk.Checkbutton(root, text = "Uncheck the checkbox if you do not wish to include intergers", variable = digits_var)
digits_check.pack()

special_var = tk.BooleanVar()
special_var.set(True)
special_check = tk.Checkbutton(root, text = "Uncheck the checkbox if you do not wish to include punctuation marks", variable = special_var)
special_check.pack()

#Generate Password button
generate_button = tk.Button(root, text = "Generate Password", command = generate_password_click)
generate_button.pack(pady=10)

#Display password
password_display_label = tk.Label(root, text = "")
password_display_label.pack(pady=5)

root.mainloop()
