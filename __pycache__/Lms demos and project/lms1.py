from cgitb import text
from tkinter import *
root=Tk()
root.geometry("1024x768")


def submit():
    print("S")



Welcome=Label(text="Welcome To LMS",font=("Arial",50)).grid(row=2,column=5)
#display
username=Label(root,text="Username",font=("Arial Black",50)).grid(row=3,column=4)
password=Label(root,text="Password",font=("Arial Black",50)).grid(row=4,column=4)

#ValueType
username_input=StringVar()
password_input=StringVar()

#entry
Entry_username=Entry(root,textvariable=username_input).grid(row=3,column=5)
Entry_password=Entry(root,textvariable=password_input).grid(row=4,column=5)

Button1=Button(text="Submit",command="submit").grid(row=5,column=5)
root.mainloop()
