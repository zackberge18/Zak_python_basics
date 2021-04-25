from tkinter import *
import datetime
import time
import winsound

clock=Tk()
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time=datetime.datetime.now()
        now=current_time.strftime("%H:%M:%S")
        date=current_time.strftime("%d/%m/%y")
        print("the set date is:",date)
        print(now)
        if now==set_alarm_timer:
            print("time to wake up")
            my_label=Label(clock,text="time to wake up")
            my_label.pack()
            winsound.PlaySound("sound.waw",winsound.SND_ASYNC)
            break
def actual_time():
    set_alarm_timer=f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock.title('data flair alarm clock')
clock.geometry("400x200")
time_format=Label(clock,text="Enter time in 24 hhour fomat: ",fg="red",bg="black",font="arial").place(x=60,y=120)
setYourAlarm=Label(clock,text="when to wake up: ",fg="blue",relief="solid",font=("Helevetica",7,"bold")).place(x=0,y=29)

#The variables we require to set the alarm(initialization):

hour=StringVar()
min=StringVar()
sec=StringVar()

#time required to set the alarm clock:
hourTime=Entry(clock,textvariable=hour).place(x=110,y=30)
minTime=Entry(clock,textvariable=min).place(x=150,y=30)
secTime=Entry(clock,textvariable=sec).place(x=200,y=30)

#to take inpt by user
submit=Button(clock,text="set alarm",command=actual_time)
submit.place(x=110,y=70)
clock.mainloop()
