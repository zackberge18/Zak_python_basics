from tkinter import *

root=Tk()
def photographer():
    animals= input('enter a animal name : ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name= input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    text1='say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind'
    new_label=Label(root,text=text1)
    new_label.pack()
my_Label=Label(root,text="welcome to Madlib")
my_Label.pack()
my_Button=Button(root,text="photographer",command=photographer)
my_Button.pack()
root.mainloop()