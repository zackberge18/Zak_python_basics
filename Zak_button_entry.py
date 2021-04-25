from tkinter import *


root=Tk()
e=Entry(root,width=50,bg="grey")
e.pack()
e.insert(0,"enter your name")
def myClick():
    hello="Hello "+e.get()
    myLabel=Label(root,text=hello)
    myLabel.pack()
myButton=Button(root,text="click me",command=myClick)
myButton.pack()
root.mainloop()
