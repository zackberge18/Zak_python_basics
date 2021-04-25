# 0 1 1 2 3 5 8 13 21 34
fibonacci=[0,1]
n=0
while True:
    x=fibonacci[n]+fibonacci[n+1]
    fibonacci.append(x)
    n+=1
    if len(fibonacci)==10:
        break
print(fibonacci)

#fibonacci was created succesfully

#check prime number for each fibonacci nums
for num in fibonacci:
    if num<=1:
        continue
    if num==2:
        continue
    if num>2 and num%2==0:
        continue
    for i in range(3,num,2):
        if num %i==0:
            break
    else:
        print("the number is prime",num)
