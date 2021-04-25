"""from tkinter import *
import random,string
import pyperclip

root=Tk()
root.title("password generator")
root.geometry("400x500")
root.resizable(0,0)

Label(root,text="PASSWORD GENERATOR",font="arial 20 bold").pack()
Label(root,text="ZACK BERGE",font="arial 12 bold").pack(side=BOTTOM)


pass_label=Label(root,text="PASSWORD LENGHT",font="arial 10 bold").pack()
pass_len=IntVar()
lenght=Spinbox(root,from_=8,to_=32,textvariable=pass_len,width=10).pack()

pass_str=StringVar()
def Generator():
    password=''

    for x in range(0,4):
        password=random.choice(string.ascii_uppercase)\
                 +random.choice(string.ascii_lowercase)\
                 +random.choice(string.digits)\
                 +random.choice(string.punctuation)
    for y in range(pass_len.get()-4):
        password=password\
                 +random.choice(string.digits)
    pass_str.set(password)


Button(root,text="Generate",command=Generator).pack(pady=5)

Entry(root,textvariable=pass_str,width=30).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)



root.mainloop()


"""
"""
from tkinter import *
import random,string
import pyperclip

root= Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("password generator")
def Generate():
    a = int(pass_lenght.get())

    password=''
    for i in range(int(a)):
        password=random.choice(string.digits)+password
    b.set(password)

def copying():
    pyperclip.copy(password_entry.get())

headline=Label(root,text="PASSWORD GENERATOR",font="arial 20 bold").pack()
b=StringVar()
pass_lenght=Entry(root,width=20)
pass_lenght.pack()
#a=int(pass_lenght.get())
#print(type(a))
generate_button=Button(root,text="generate",command=Generate).pack()

password_entry=Entry(root,width=20,textvariable=b)
password_entry.pack()

Button(root,text="copy to clipboard",command=copying).pack()
root.mainloop()
"""
from tkinter import *
import random,string
import pyperclip

root= Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("password generator")
def Generate():
    a = int(pass_lenght.get())

    password=''
    for i in range(int(a)):
        password=random.choice(string.digits)+password
    b.set(password)

def copying():
    pyperclip.copy(password_entry.get())

headline=Label(root,text="PASSWORD GENERATOR",font="arial 20 bold").pack()
b=StringVar()
pass_lenght=Spinbox(root,from_=8,to_=16)
pass_lenght.pack()

generate_button=Button(root,text="generate",command=Generate).pack()

password_entry=Entry(root,width=20,textvariable=b)
password_entry.pack()

Button(root,text="copy to clipboard",command=copying).pack()
root.mainloop()