from tkinter import *
from PIL import ImageTk,Image
import random

root=Tk()
root.title("roll dice stimulation")
root.iconbitmap("images/pac-man.ico")
root.geometry("600x800")

def roll_dice():
    global dice_shape
    ran=random.choice(dice_list)


    dice_shape.grid_forget()
    dice_shape = Label(root, image=ran)
    dice_shape.grid(row=1, column=0)
    my_label=Label(root,text="welcome to my game", bg="red",font="bold")
    my_label.grid(row=0,column=0,columnspan=2)
    roll_button = Button(root, text="Start rolling", command=roll_dice)
    roll_button.grid(row=2, column=0)


img_dice_1=ImageTk.PhotoImage(Image.open("images/dice1.webp"))
img_dice_2=ImageTk.PhotoImage(Image.open("images/dice2.png"))
img_dice_3=ImageTk.PhotoImage(Image.open("images/dice3.png"))
img_dice_4=ImageTk.PhotoImage(Image.open("images/dice4_new.png"))

dice_list=[
    img_dice_1,
    img_dice_2,
    img_dice_3,
    img_dice_4
]

dice_shape=Label(root,image=img_dice_4)
dice_shape.grid(row=0,column=0)

roll_button=Button(root,text="Start rolling",command=roll_dice)
roll_button.grid(row=1,column=0)


root.mainloop()