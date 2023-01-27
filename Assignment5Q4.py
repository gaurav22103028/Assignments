# without using nested for loop
# for i in range (1,6):
#     print("* "*i)
# i=4
# while(i>0):
#     print("* "*i)
#     i=i-1
n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("")
for i in range(n-1):
    for j in range(n-1-i):
        print("*",end=" ")
    print("")