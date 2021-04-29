from tkinter import *
from gtts import gTTS
from playsound import playsound


root=Tk()
root.geometry("600x500")
root.resizable(0,0)
root.configure(bg="red")
root.title(" my teext to speech")
font="arial 15 bold"
Label(root,text="text to speech ",font=font,bg="blue",width=20).pack(side="bottom")
Label(root,text="Enter tExt",font=font,bg="white smoke",width=30).pack(side="top")
Msg=StringVar()


def Txt_to_spch():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save("uck.mp3")
    playsound("uck.mp3")


def reset():
    Msg.set("")
entry_field=Entry(root,textvariable=Msg,width=45)
entry_field.place(x=180,y=56)
play_button = Button(root, text="PLAY", font=font,command=Txt_to_spch,width=26).place(x=170,y=100)

root.mainloop()