x= [int(x) for x in input("Enter 10 integers seperated by space:").split()]
#a)
print("Positive numbers are:",end="")
for i in x:
    if i>0:
        print(i,end=",")
print("")
#b)
print("Negative numbers are:",end="")
for i in x:
    if i<0:
        print(i,end=",")
print("")
#c)
print("Odd numbers are:",end="")
for i in x:
    if(i%2!=0):
        print(i,end=",")
print("")
#d)
print("Even numbers are:",end="")
for i in x:
    if(i%2==0):
        print(i,end=",")
print("")
#e)
diction=dict()
for i in x:
    if i in diction:
        diction[i]=diction[i]+1
        continue
    diction[i] = 1
print(diction)
