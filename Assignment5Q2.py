a, b = input("Enter the range seperated by comma:").split(",")
a= int(a)
b= int(b)
n= int(input("Enter the number:"))
for i in range(a,b+1):
    if(i%n==0):
        print(i,end=",")