from cgitb import text
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from tkinter.tix import TEXT, NoteBook
from turtle import st, width
from tkinter import messagebox
from tkinter import colorchooser
from click import Command, command
from flask import config
from tkinter import ttk

#function for counting the number of clicks
count=0
def ciel():
    global count#imp as without it count does not work
    count+=1
    print(count)
    print("Hi How ARE YOU?")
'''def submit():     
    username=(f"Hi{entry_1.get()}")   
    print(username)
    entry_1.config(state=DISABLED)
def delete():
    entry_1.delete(0,END)
def backspace():
    entry_1delete(len(entry_1.get())-1,END)'''





root=Tk()
root.geometry("420x400")
root.title("Hahaha")
'''icon= PhotoImage(file="logo.png")
root.iconphoto(True,icon)'''



#Label
label_1=Label(root,text="Hi how are you",font=("Arial",40,"bold"),fg="green",bg="yellow",padx=9,pady=9,compound="bottom").pack()#image=photo can also be used



#Button
button=Button(root,text="button",command=ciel,font=("Comic Sans",30),fg="black",bg="white",activebackground="black",activeforeground="white",state=ACTIVE,).pack()#image=photo
#label_1.place(X=0,Y=0)



#Entry
entry_1=Entry(root,font=("Arial",50),show="*").pack()

'''submit_button=Button(root,text="Submit").pack()

delete_button=Button(root,text="delete",command=delete).pack()
'''



#Checkbox
def variable():
    if(x.get()==1):
        print("Agree")
    else:
        print("No")


x=IntVar()
check_button=Checkbutton(root,text="check it bitch",variable=x,onvalue=0,offvalue=1,command=variable).pack()
root.config(background="aqua")



#Radiobutton()
def foodie():
    if (x.get()==0):
        print("Pizza")
    elif (x.get()==1):
        print("Burger")
    elif (x.get()==2):
        print("Hotdog")
    else:
        print("huh")
food=["pizza","burger","hotdog"]
#pizzaImage=hotoImage(file='pizza,png')
#burgerImage=hotoImage(file='burger,png')
#hotdogImage=hotoImage(file='hotdog,png')
#Fodimage=[pizzaImage,burgerImage,hotdogImage]

x=IntVar()
for i in range(len(food)):
    radio_button=Radiobutton(root,text=food[i],variable=x,value=i,indicatoron=0,command=foodie).pack()
    #give text to radio button 
    #grp radiobuttons together
    #assign diff values to radiobuttons,
    #image=Foodimage[i].....adds immage to radiobuttons
    #remove circle indicators




#SCALE
def scalee():
    print(f'scale is at "+ str{scale_1.get()}+"')
#for image at Top use th below code
#hotimage=PhotoImage(file=hbcr.png)
#hotLabel=Label(image=hotimage).pack()
scale_1=Scale(root,from_=0,to=100,orient=VERTICAL,tickinterval=20).pack()
#for image at Bottom use th below code
#potimage=PhotoImage(file=hbcr.png)
#potLabel=Label(image=potimage).pack()
btton9=Button(root,text="Submit",command=scalee).pack()



#LISTBOX
def listb():
    print(first.get(first.curselection()))
def add():
    first.insert(first.size(),entry.get())
def delete():
    first.delete(first.curselection())
    first.config(height=first)
first=Listbox(root,)
first .pack()
first.insert(1,"izza")
first.insert(1,"izza")
first.insert(4,"ifsddfzza")
first.insert(5,"oizza") 

entry=Entry(root).pack()

btn=Button(root,text="Submit",command=listb).pack()
btn2=Button(root,text="Add",command=add).pack()
btn3=Button(root,text="Delete",command=delete).pack()


 



#Messagebox
def click():
    #messagebox.showinfo(title="Message Box",message="This ia a message box")
    
    #messagebox.showwarning()(title="Message Box",message="This ia a warning box")

    #messagebox.showerror()(title="Message Box",message="This ia a error box")

    if messagebox.askokcancel(title="Message Box",message="This ia a cancel box"):
        print("true")
    else:
        print("false")

msg=Button(root,text="Click",command=click).pack()



#Textarea
text_1=Text(root,bg="grey",width="100").pack()





#Fieldialog
#def openFile():
    #filepath=filedialog.askopenfilename(initialdir=".......")
    #file=open(filepath,"r")
    #print(file.read())
    #file.close()


#button=Button(text="Open",command=openFile).pack()

'''




#fileDialogue Save




'''


#MenuBar
menubar=Menu(root)
root.config(menu=menubar)
'''
openinamge=PhotoImage(file="filename")
saveimage=PhotoImage(file="filename")

'''
file_menu=Menu(menubar)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New")#image=openimage
file_menu.add_separator()
file_menu.add_command(label="Save")#image=saveimage
file_menu.add_separator()
file_menu.add_command(label="Save As")


edit_menu=Menu(menubar)
menubar.add_cascade(menu=edit_menu,label="Edit")
edit_menu.add_command(label="Copy")
edit_menu.add_separator()
edit_menu.add_command(label="Undo")


View_menu=Menu(menubar)
menubar.add_cascade(label="Edit",menu=View_menu)
edit_menu.add_command(label="Copy")
edit_menu.add_separator()
edit_menu.add_command(label="Undo")




#Frame
frame=Frame(root,bg="pink",bd=5,relief=SUNKEN)
frame.place(x=100,y=0)
button_6=Button(frame,text="W",font=("Consolas",25),width=10).pack(side=TOP)
button_5=Button(frame,text="B",font=("Consolas",25),width=10).pack(side=LEFT)
button_4=Button(frame,text="L",font=("Consolas",25),width=10).pack(side=LEFT)




#open new window
def create_window():
    new_window=Toplevel()#it creates new window on top og other windows
    old_window.destroy()
old_window=Tk()
#Tk() is a new independent window

button__3=Button(root,command=create_window).pack()





'''
#window tabs
notebook=NoteBook(root)#it manages a collection of windows/displays
tab1=Frame(notebook)
tab2=Frame(notebook)

notebook.add(tab1,text="Tab1")
notebook.add(tab2,text="Tab2")
notebook.pack(expand=True)

Label(tab1,text="hello paaji ki haal").pack()
Label(tab2,text="Ahan Ahan").pack()
root.mainloop()  '''



#grid 
first_name=Label(root,text="Name").grid(row=0,column=0)
first_nameEntry=Entry(root).grid(row=1,column=0)





root.mainloop()