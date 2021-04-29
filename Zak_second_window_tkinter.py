""""from tkinter import *
from PIL import ImageTk,Image


root=Tk()
r=IntVar()
r.set("2")

def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()

Radiobutton(root,text="option 1",variable=r,value=1,command=lambda : clicked(r.get())).pack()
Radiobutton(root,text="option 2",variable=r,value=2,command=lambda : clicked(r.get())).pack()
Radiobutton(root,text="option 3",variable=r,value=3,command=lambda : clicked(r.get())).pack()

my_label = Label(root, text=r.get())
my_label.pack()

root.mainloop()"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root=Tk()

def fuck():
    global my_image
    top = Toplevel()
    top.title("my second window")
    my_image = ImageTk.PhotoImage(Image.open("spaceship_yellow.png"))
    my_label = Label(top, image=my_image).pack()
    btn2=Button(top,text="destroy",command=top.quit)
    btn2.pack()

my_button=Button(root,text="Open Second Window",command=fuck)
my_button.pack()
hell_no=filedialog.askopenfilename(title="select a file",filetypes=(("png files","*.png"),("all filesss","*.*")))
miLa=Label(root,text=hell_no).pack()

root.mainloop()
