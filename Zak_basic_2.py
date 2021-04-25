#########22
#given_list=[3,4,5,6,7,4,8,4]
#is_for=[ i==4 for i in given_list]
#
#count_for_4=0
#print(is_for)
##new_list=[i for i in given_list if i==4 ]
##print(new_list)



#########23
#given_string=input("something :")
#if len(given_string<=2:
#    print(4*given_string)
#print(4*given_string[0:2])



#####24
#letter=input("wrrite down sometihng :").lower()
#if letter=="a" or letter=="e" or letter=="i" \
#        or letter=="u" or letter=="o":
#    print(letter, "is a vower")
#else:
#    print("it is constant")



########25
#test_data=[1,23,4,5,6,7]
#value=int(input("enter a number: "))
#if value in test_data:
#    print(True)
#else:
#    False


#########26
#histogram_shape="%"
#my_list=[1,2,5,6,7,12]
#for i in my_list:
#    print(i*histogram_shape)



######27
#my_list=["se","er","fuc","you"]
#my_str=""
#for i in my_list:
#    my_str=my_str+i
#print(my_str)


#######28
#numbers = [
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#    958,743, 527
#    ]
#for i in range(len(numbers)):
#    if numbers[i]==237 and numbers[i+1]%2==0:
#        break
#    if numbers[i]%2==0:
#        print(numbers[i])


######29

#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
#a=color_list_1.difference(color_list_2)
#print(a)


#######30
#base=int(input("base: "))
#height=int(input("height :"))
#print(base*height*1/2)


########31
#Write a Python program to compute the greatest common divisor (GCD) of two positive integers. Go to the editor


######32
#Write a Python program to get the least common multiple (LCM) of two positive integer


########33
#def sum(x,y,z):
#    if x==y and y==z and x==z:
#        print(0)
#    else:
#        print(x+y+z)
#sum(3,4,5)

########34
#def total(a,b):
#    if a+b>=15 and a+b<=20:
#        print(20)
#    else:
#        print(a+b)
#total(23,46)

########35

#def func(a,b):
#    if a==b or a+b==5 or b-a==5 or a-b==5:
#        print(True)
#
#func(4,1)
#
#######36
#def func(a,b):
#    try :
#        print(int(a)+int(b))
#    except:
#        print("enter a number")
#
#func(4,"asdf")

#######37
#def details(a="uke",b=21,c="crested butte"):
#    detail_list=[a,b,c]
#    print(f"{a} \n {b} \n{c}")
#
#details("zack",23,"idahospring")
#
#


#######38
#def func(x,y):
#    answer=(x+y)*(x+y)
#    print("(x+y)^2=",answer)
#func(5,7)

######39
#amt = 10000
#int = 3.5
#years = 7
#
#future_value  = amt*((1+(0.01*int)) ** years)
#print(round(future_value,2))
#
#####40

#def distance(x1,x2,y1,y2):
#    new=(abs(x2-x1)/2,abs(y2-y1)/2)
#    print(new)
#
#distance(3,5,5,7)

#######41
#import os.path
#
#print(os.path.isfile('images/pac-man.'))
#
########42
## For 32 bit it will return 32 and for 64 bit it will return 64
#import struct
#print(struct.calcsize("P") * 8)


#########43
#import platform
#import os
#print(os.name)
#print(platform.system())
#print(platform.release())


####### 44
#import site
#print(site.getsitepackages())
#

######45
#rom subprocess import call
#all(["ls", "-l"])


######46
#import os
#print("file name",os.path.relpath(__file__))

######47
#import multiprocessing
#print(multiprocessing.cpu_count())

#48
#49
#from os import listdir
#from os.path import isfile, join
#files_list = [f for f in listdir('/images/pac-man.ico') if isfile(join('/images', f))]
#print(files_list);


####50

####51
#import cProfile
#def sum():
#    print(1+2)
#cProfile.run('sum()')

#52
"""
    import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

"""
########53

"""import os
# Access all environment variables
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')
"""


######60


"""import math

class hipotenus:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def hipo(self):
        self.a=math.sqrt(math.pow(self.x,2)+math.pow(self.y,2))
    def pr(self):
        print(self.a)


ef=hipotenus(3,4)

ef.hipo()
ef.pr()
"""

#####61
"""import os
class absulate:

        def __init__(self,x):
            self.x=x

        def path(self):
            self.a=os.path.relpath(f"{self.x}")
        def print_doc(self):
            print(self.a)

path1=absulate("abc.txt")
path1.path()
path1.print_doc()"""

####64

"""import os
import time
print(f"last modified : {time.ctime(os.path.getmtime('abc.txt'))}")
print(f"last created : {time.ctime(os.path.getctime('abc.txt'))}")
"""

######65
"""
time=float(input("imput time in seonds:"))
day=time//(24*3600)
time=time%(24*3600)
hour=time//3600
time=time%3600
minutes=time//60
time%=60
second=time

print(f"d:h:m:s >>>{day}:{hour}:{minutes}:{second} ")

print(10//7)
print(10/7)
print(10%7)"""


"""import getpass
print(getpass.getuser())"""

"""import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("Time to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))
"""

"""class bmi:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def calc(self):
        self.ans=round(self.x*(self.y**2),2)

    def show(self):
        print((self.ans))

person=bmi(45,184)

person.calc()
person.show()"""
"""
class mat():

    def __init__(self,number):
        self.number=number

    def digit(self):
        self.count=0
        for i in self.new_num:
            self.count+=int(i)

    def int_str(self):
        self.new_num=str(self.number)

    def show(self):
        print((self.count))

my_number=mat(54321)

my_number.int_str()
my_number.digit()
my_number.show()

num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1* )//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)"""


#class mat():
#
#    def __init__(self,num1,num2,num3):
#        self.num1=num1
#        self.num2=num2
#        self.num3=num3
#    def make_list(self):
#        self.my_list=list([self.num2,self.num1,self.num3])
#
#    #def line(self):
#    #    self.new_list=sorted(self.my_list)
#
#    def basic_sort(self):
#
#        self.basic_list=[self.min_num,self.mid,self.max_num]
#
#    def other_method(self):
#        self.max_num=max(self.my_list)
#        self.min_num=min(self.my_list)
#        self.mid=sum(self.my_list)-self.max_num-self.min_num
#
#
#    def show(self):
#        print((self.basic_list))
#
#nums=mat(23,45,11)
#nums.make_list()
#nums.other_method()
#nums.basic_sort()
#nums.show()

#import glob
#import os
#
#files = glob.glob("*.txt")
#files.sort(key=os.path.getmtime)
#print("\n".join(files))
#


#######70
#from stat import S_ISREG, ST_CTIME, ST_MODE
#import os, sys, time
#
##Relative or absolute path to the directory
#dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
#
##all entries in the directory w/ stats
#data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
#data = ((os.stat(path), path) for path in data)
#
## regular files, insert creation date
#data = ((stat[ST_CTIME], path)
#           for stat, path in data if S_ISREG(stat[ST_MODE]))
#
#for cdate, path in sorted(data):
#    print(time.ctime(cdate), os.path.basename(path))

"""
#IMports  the math module
import math
#Sets everything to a list of math module
math_ls=dir(math)
print(math_ls)
"""

#def midpoint_formula(t,k):
#    formula_x=(t[0]+k[0])/2
#    formula_y=(t[1]+k[1])/2
#    print(formula_x,formula_y)
#
#midpoint_formula((1,2),(3,4))

#import sys
#print("\nPython Copyright Information")
#print(sys.copyright)
#print()

"""import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))"""

#import sys
#import textwrap
#module_name = ', '.join(sorted(sys.builtin_module_names))
#print(textwrap.fill(module_name, width=70))
"""import sys
print(sys.getrecursionlimit())"""
#list_color="i hate you"
#a=list_color.split(" ")
#colors="@@".join(a)
#print("al coloros",colors)


#82
#a=sum([23,45,67])
#print(a)

#83
#import numpy as np
#def test():
#    print(my_list[my_list>45])
#
#my_list=np.array([23,45,6,7,89,9,7,6,34,55,33,12,34])
#test()
#import numpy as np
#my_list=np.array([1,2,3,5,6,7,8])
#mask_list=[True if x>5 else False for x in my_list]
#a=my_list[mask_list]
#print(a)
#
#"""vec = [[1,2,3], [4,5,6], [7,8,9]]
#print([num for elem in vec for num in elem])"""


########84
#def func(x):
#    count=0
#    for i in x:
#        if i=="a":
#            count+=1
#    print(count)
#
#test="asfgadsgdndfhdagagwryoirfdkmv"
#a=test.count("a")
#print(a)

#import os
#path="images"
#if os.path.isdir(path):
#    print("\nIt is a directory")
#elif os.path.isfile(path):
#    print("\nIt is a normal file")
#else:
#    print("It is a special file (socket, FIFO, device file)" )
#print()

#86

#import os
#def check(x):
#    if os.path.isdir(x):
#        print("directory")
#    elif os.path.isfile(x):
#        print("file")
#    else:
#        print("fcuk you")
#path="Zak_password_genarator.py"
#check(path)

#86

#import string
#print(string.ascii_letters)
#import os
#print(os.path.getsize("Zak_password_genarator.py"))
#
##87
#x=67
#y=43
#print("%d+%d=%d"%(x,y,x+y))
#


########89##########

