import tkinter as tk
from tkinter import *
from pytube import YouTube
import base64


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        Label(text="fuck you").pack()


if __name__  ==  "__main__":
    app = App()
    app.mainloop()