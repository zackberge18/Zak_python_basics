import tkinter as tk
from tkinter import *
from pytube import YouTube


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.font="arial 20 bold"
        Label(text="Youtube Video downloader",font=self.font).pack()
        self.geometry("500x300")
        self.resizable(0,0)
        self.title("MY downloader")
        self.link=StringVar()
        Label(text="Paste here",font=self.font)
        self.link_enter=Entry(width=70,textvariable=self.link)
        self.link_enter.pack()
        Button(text="download",command=self.DownloaD,padx=10,pady=10).pack()

        
    def DownloaD(self):
        self.url=YouTube(str(self.link.get()))
        self.video=self.url.streams.first()
        self.video.download()
        Label(text="Success",font=self.font).pack()






if __name__  ==  "__main__":
    app = App()
    app.mainloop()