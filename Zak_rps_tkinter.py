from tkinter import *
import random
root=Tk()
root.geometry("800x800")
root.resizable(0,0)
root.title("dataFlaite")
root.config(bg='seashell3')
game=["rock",'paper','scissors']
global cp_choice
def button_rock():
    cp_choice = random.choice(game)
    if cp_choice=="paper":
        myLabel=Label(root,text="cp win")
        myLabel.pack()
    elif cp_choice=="rock":
        myLabel = Label(root, text="tie")
        myLabel.pack()
    else:
        myLabel = Label(root, text="you win")
        myLabel.pack()
def button_paper():
    cp_choice = random.choice(game)
    if cp_choice == "paper":
        myLabel = Label(root, text="tie")
        myLabel.pack()
    elif cp_choice == "rock":
        myLabel = Label(root, text="you win")
        myLabel.pack()
    else:
        myLabel = Label(root, text="cp win")
        myLabel.pack()
def button_scissors():
    cp_choice = random.choice(game)
    if cp_choice == "paper":
        myLabel = Label(root, text="you win")
        myLabel.pack()
    elif cp_choice == "rock":
        myLabel = Label(root, text="cp win")
        myLabel.pack()
    else:
        myLabel = Label(root, text="tie")
        myLabel.pack()

Label(root,text="Rock, Paper, Scissors",font="arial 20 bold",bg="seashell2").pack()
button_rock=Button(root,text="rock",padx=40,pady=20,command=button_rock)
button_paper=Button(root,text="paper",padx=40,pady=20,command=button_paper)
button_scissors=Button(root,text="scissors",padx=40,pady=20,command=button_scissors)
button_paper.pack()
button_rock.pack()
button_scissors.pack()
root.mainloop()
