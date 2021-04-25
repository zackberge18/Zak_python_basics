"""import numpy as np
arr1=np.array([2,6,8,1,3])
arr2=arr1.view()
arr1[1]=7

print(arr1)
print(arr2)

arr1=np.array([

    [1,2,3,5,6,7],
    [4,5,6,3,6,7]
])

arr2=arr1.flatten()

arr3=arr2.reshape(2,2,3)

print(arr3)


arr1=np.array([
    [1,2,3,6],
    [4,5,6,7]
])

m=np.matrix('1 2 3 ; 6 4 5 ; 1 6 7 ')
m2=np.matrix('1 2 3 ; 6 3 5 ; 1 1 6 ')
print(np.diagonal(m))
print(m.max())
m3=m2+m
print(m3)
"""

"""def sum(a,*b): # *b is tuple format data
    c=a
    for i in b:
        c=c+i
    return print(c)

sum(4,5,6,7,8,8,9,0)
"""

"""def person(name, **data):

    print(name)
    for i,j in data.items():
        print(i,j)
    print(data)

person("navin",age=28,city="mumbai",mob=98779)"""
#a=10
#def something():
#    a=9
#
#    x=globals()['a']
#    print("in fun",a)
#    print("in fun",x)
#
#print("outside", a)
#something()
#
#print("outside", a)


#list=[1,2,3,44,12,4,55,6,4,3,21,23,55,7]
#
#def count(list):
#    even,odd=0,0
#    for i in list:
#        if i%2==0:
#            even+=1
#
#        else:
#            odd+=1
#
#    return even,odd
#
#even,odd=count(list)
#print(even,odd)


#def fib(n):
#    list=[0,1]
#    for i in range(n):
#        list.append(list[i]+list[i+1])
#    print(list)
#
#fib(10)

#def fib(n):
#    a=0
#    b=1
#
#    for i in range(2,n):
#        c=a+b
#        a=b
#        b=c
#        if c>100:
#            break
#        print(c)
#
#
#fib(100)

#def fact(x):
#    fact=1
#    for i in range(1,x):
#        fact=i*fact
#
#    return fact
#
#x=5
#result=fact(5)
#
#print(result)

#import sys
#
#sys.setrecursionlimit(2000)
#
#print(sys.getrecursionlimit())
#
#i=0
#def greet():
#    global i
#    i+=1
#    print("hello")
#    greet()
#
#greet()
#   def fact(n):
#       if n==0:
#           return 1
#       return n*fact(n-1)
#
#
#
#   result =fact(5)
#   print(result)

# square=lambda a: a*a
# print(square(5))
#
# plus_ultra=lambda b,r,e:b+r+e
#
# eve=plus_ultra(23,44,56)
# print(eve)
# from functools import reduce
#
# nums = [3, 45, 32, 12, 6]
# evens = list(filter(lambda n: n % 2 == 0, nums))
#
# doubles = list(map(lambda n:n*2,nums))
# sum=reduce (lambda a,b : a+b,doubles)
#
# print(evens)
# print(sum)

"""
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.cpu+self.brand,self.ram)


s1=Student("navin",2)
s2=Student("jenny",3)
lap1=Student.Laptop()

s1.show()
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title="LEarn to at Codemy.com"
root.iconbitmap("icon-icons.ico")
my_img = ImageTk.PhotoImage(Image.open("images/a.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("images/b.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/c.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/d.png"))
my_img4= ImageTk.PhotoImage(Image.open("images/e.png"))
image_list=[my_img2,my_img3,my_img1,my_img]

status=Label(root,text="image"+"1"+"of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=W)
my_label=Label(image=my_img2)
my_label.grid(row=0,column=0,columnspan=3)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",command=lambda : forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: forward(image_number-1))
    button_back.grid(row=1, column=0)
    status = Label(root, text="image" + str(image_number) + "of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)
def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[ 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: forward(image_number - 1))
    button_back.grid(row=1, column=0)
    status = Label(root, text="image" + str(image_number) + "of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)


button_back=Button(root,text="<<",command=back)
button_forward=Button(root,text=">>",command=lambda :forward(2))

button_quit=Button(root,text="Exit program",command=root.quit)

button_back.grid(row=1,column=0)

button_forward.grid(row=1,column=2,pady=10)

button_quit.grid(row=1,column=1)



root.mainloop()


