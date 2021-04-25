import sys

########1
# print(sys.version)


import datetime
#########2
#date=datetime.datetime.now()

#print("current date and time: ",date)

import math
#########3
# radius=int(input("cal area : "))
# area= math.pi*pow(radius,2)
# print(area)

########4

#name=input("first name: ")
#last=input("last name : ")
#print(f"{last} {name}")

########4.1
#first=input("first :")
#last=input("last :")
#
#first_list=[i  for i in first]
#last_list=[i for i in last]
#first_list.reverse()
#last_list.reverse()
#a="".join(first_list)
#b="".join(last_list)
#print(a+" " +b)

##########5
#seq=input("enter your sequance : ")
#arr=seq.split(",")
#tup=tuple(arr)
#print(arr)
#print(tup)



#########6

#file_name=input("nter file name :")
#file_ext=file_name.split(".")
#print(file_ext[-1])


########7
#color_list=["kesk","sor","zer","pirtakan"]
#print(color_list[0],color_list[-1])
#print(color_list[0::3])



#######8
#exam_st_date = (4,17,2021)
#print(f"examination date: {exam_st_date[0]}:{exam_st_date[1]}:{exam_st_date[2]}")



#######9
#num=input("enter a num: ")
#num_2=num*2
#num_3=num*3
#total=int(num)+int(num_2)+int(num_3)
#print(total)





#########10
#print(type.__doc__)
#a=5
#print(type(a))




######11
#import calendar
#
#year=2021
#month=4
#
#cal=calendar.month(year,month)
#print(cal)



#######12
#a="""asdf
#sfdaf
#asdfsdf  wegewg
#ewtgretgwbe
#webb
#"""
#print(a)





#######13

import datetime
#import time
#first_date=input("enter the date :")
#second_date=input("enter the date :")
#first=first_date.split(":")
#second=second_date.split(":")
#int_first=[]
#int_second=[]
#
#for i in first:
#    int_first.append(int(i))
#for i in second:
#    int_second.append(int(i))
#
#date=datetime.date(int_first[0],int_first[1],int_first[2])
#date2=datetime.date(int_second[0],int_second[1],int_second[2])
#diff=date2-date
#print(diff.days)


#######14

from math import pi

#radius=int(input("enter radius: "))
#vol=4/3*pi*radius
#print(vol)


#######15

#num=int(input("number :"))
#
#if num >17:
#    print((num-17)*2)
#else:
#    print(abs(num-17))



###########16
#um=int(input("enter a number: "))
#f num>100 and num<1000:
#   print("100 to 1000")
#lse:
#   if num>100 and num<2000:
#       print("between 2000")



##########17
#nums=input("enter three num:")
#
#list=nums.split(" ")
#count=0
#
#for i in list:
#    count=int(i)+count
#    if count==3*int(i):
#        print(9*int(i))
#        break
#else:
#    print(count)


#######18
#str=input("give a string:")
#if str[0:2]=="Is" or str[0:2]=="is":
#    print(str)
#else:
#    new_str="Is"+str
#    print(new_str)


#######19
#def three_times(str):
#    return 3*str
#
#str="i hate you all"
#a=three_times(str)
#print(a)

########20

#num = int(input("giva an number:"))
#
#if num%2==0:
#    print("even")
#else:
#    print("odd")

