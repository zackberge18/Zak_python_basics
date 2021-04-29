from Zak_oop_tkinter import *
from Zak_oop_tkinter import Tk
from PIL import ImageTk,Image
from gtts import gTTS
from playsound import playsound
import os

class MyFirstGui:
    def __init__(self,master):
        self.master=master
        master.title("text to speech")
        master.geometry("500x500")
        master.resizable(0,0)
        master.configure(bg="ghost white")
        self.Msg=StringVar()
        self.text_label= Label(text="Enter text",font="arial 14 bold",width=20,padx=10,pady=10)
        self.text_label.place(x=140,y=50)
        self.entry_field= Entry(textvariable=self.Msg,width=40)
        self.entry_field.place(x=150,y=100)
        self.my_button=Button(text="Click me",command=self.translate)
        self.my_button.place(x=160,y=135)

    def translate(self):
        self.Message=self.entry_field.get()
        speech=gTTS(text=self.Message)
        self.mess=str(self.Message)
        speech.save(f"{self.mess[0:4]}.mp3")
        playsound(f"{self.mess[0:4]}.mp3")
        self.reset()
       # a=os.path.isfile(f"{self.Msg[1:4]}.mp3")
       # if a==True:
       #     os.remove("translate.mp3")
    def reset(self):
        self.Msg.set("")



root=Tk()
my_gui=MyFirstGui(root)
root.mainloop()