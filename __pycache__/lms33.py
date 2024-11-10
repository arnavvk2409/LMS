import tkinter as tk
from tkinter import messagebox

# Sample user database (for demonstration purposes only)
user_db = {}

def signup():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in user_db:
        messagebox.showerror("Error", "User  already exists!")
    elif username == "" or password == "":
        messagebox.showerror("Error", "Please fill out all fields!")
    else:
        user_db[username] = password
        messagebox.showinfo("Success", "User  registered successfully!")
        clear_entries()

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in user_db and user_db[username] == password:
        messagebox.showinfo("Success", "Login successful!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

def clear_entries():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Login and Sign Up")

# Create and place the labels and entry widgets for username and password
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the buttons for login and sign up
signup_button = tk.Button(root, text="Sign Up", command=signup)
signup_button.grid(row=2, column=0, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=1, padx=10, pady=10)

# Run the application
root.mainloop()