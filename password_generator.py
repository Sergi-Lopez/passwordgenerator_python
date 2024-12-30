import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    if not (use_uppercase or use_lowercase or use_numbers or use_symbols):
        messagebox.showerror("Error", "Please select at least one character type!")
        return

    char_pool = ""
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    password = "".join(random.choice(char_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    update_password_strength(password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

def update_password_strength(password):
    strength = calculate_password_strength(password)
    if strength <= 2:
        strength_label.config(text="Password Strength: Weak", fg="red")
    elif strength <= 4:
        strength_label.config(text="Password Strength: Moderate", fg="orange")
    else:
        strength_label.config(text="Password Strength: Strong", fg="green")

def calculate_password_strength(password):
    strength = 0
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1
    if len(password) >= 12:
        strength += 1
    return strength

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

length_var = tk.IntVar(value=8)
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

frame_options = tk.Frame(root)
frame_options.pack(pady=10)

length_label = tk.Label(frame_options, text="Password Length:")
length_label.grid(row=0, column=0, padx=5)

length_spinbox = tk.Spinbox(frame_options, from_=4, to_=128, textvariable=length_var, width=5)
length_spinbox.grid(row=0, column=1, padx=5)

uppercase_check = tk.Checkbutton(frame_options, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, columnspan=2, sticky="w")

lowercase_check = tk.Checkbutton(frame_options, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.grid(row=2, column=0, columnspan=2, sticky="w")

numbers_check = tk.Checkbutton(frame_options, text="Include Numbers", variable=numbers_var)
numbers_check.grid(row=3, column=0, columnspan=2, sticky="w")

symbols_check = tk.Checkbutton(frame_options, text="Include Symbols", variable=symbols_var)
symbols_check.grid(row=4, column=0, columnspan=2, sticky="w")


password_frame = tk.Frame(root)
password_frame.pack(pady=10)

password_entry = tk.Entry(password_frame, width=30, font=("Arial", 12))
password_entry.pack(side="left", padx=5)

copy_button = tk.Button(password_frame, text="Copy", command=copy_to_clipboard)
copy_button.pack(side="right", padx=5)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)


strength_label = tk.Label(root, text="Password Strength: ", font=("Arial", 10))
strength_label.pack(pady=5)

root.mainloop()
