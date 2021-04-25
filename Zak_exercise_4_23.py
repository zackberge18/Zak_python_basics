"""nums=[10,18,21,23]
for num in nums:

    if num %5==0:
        print(num)
        break
else:
    print("not found")


"""
"""nums=[7,10,11]
for num in nums:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    else:
        print("prime")

"""
"""import time
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i==0:
            return False
    return True
t0=time.time()
c=0 #for counting

for n in range(1,100000):
    x=is_prime(n)
    c+=x
print("total prime number : ",c)
t1=time.time()
print("total time required: ",t1-t0)
"""

"""import math
import time

def is_prime(n):
    if n<=1:
        return False

    max_div=math.floor(math.sqrt(n))
    for i in range(2,1+max_div):
        if n%i==0:
            return False
    return True
t0=time.time()
c=0 #for counting

for n in range(1,100000):
    x=is_prime(n)
    c+=x
print("total prime number : ",c)
t1=time.time()
print("total time required: ",t1-t0)"""

"""import time
import math

def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0:
        return False
    max_div=math.floor(math.sqrt(n))
    for i in range(3,1+max_div,2):
        if n%i==0:
            return False
    return True

t0=time.time()
c=0

for n in range(1,100000):
    x=is_prime(n)
    c+=x
print(c)
t1=time.time()
print("time is :",t1-t0)"""

"""from array import *
vals=array('i',[5,4,3,-5,6])
vals.reverse()
print(vals)"""



""" ####for loop###
x=['navin',65,57]

for i in x:
    print(i)
"""
import tkinter

"""for i in range(10,0,-2):
    if i%5!=0:
        print(i)"""

"""for i in range(200):
    if i*i<200:
        print(i)"""

"""x=int(input("how many candies you want: "))
av=3
i=1
while i<=x:
    if i>av:
        print("out of stock")
        break
    print('candy')
    i+=1
print("bye")"""
"""for i in range(100):
    if i%3==0:
        continue
    else:
        print(i)"""
"""a,b=0,1
fibonacci=[0,1]
while True:
    if len(fibonacci)>10:
        break
    fibonacci.append((a+b))
    x=a
    a=b
    b=x+b

for num in fibonacci:
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
"""

"""x=[0,1,1,2,3,5,8,13,21]

for i in x:
    for b in range(i):
        if b%2==0 and b>1 :
            break
    else:
        print(x)"""
"""from tkinter import *
root=Tk()
root.geometry('300x300')
root.title("data")
tkinter.Label(root,text="madlib ").pack()
tkinter.Label(root,text='click anyone').place(x=40,y=80)

def madlib1():
    animals = input('enter a animal name : ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name = input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    print(
        'say ' + food + ', the photographer said as the camera flashed! \n'
                        '' + name + ' and I had gone to ' + place + ' to get our photos \n'
        'taken on my birthday. The first photo we really wanted was a picture of\n'
        ' us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')
    tkinter.Button(root,text='The photographer ',command=madlib1).place(x=60,y=120)
root.mainloop()
"""
import math
x=math.ceil(4.01)
print(x)