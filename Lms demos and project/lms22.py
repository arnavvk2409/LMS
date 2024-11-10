import tkinter as tk
from tkinter import messagebox

# Predefined user data (username: password)
user_data = {
    "user1": "password1",
    "user2": "password2",
    "admin": "adminpass"
}

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()
        # Check if the username exists and the password matches
    if username in user_data and user_data[username] == password:
       messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("1024x768")

# Create and place the username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Create and place the password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

# Run the application
root.mainloop()