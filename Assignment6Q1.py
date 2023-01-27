n = int(input("Enter the number:"))
sum=0
# for i in range(1,n):
#     if(n%i==0):
#         sum=sum+i
# if(n==sum):
#     print("It is a perfect number.")
# else:
#     print("It is not a perfect number.")
for i in range(1,n+1):
    if(n%i==0):
        sum=sum+i
if(n==(sum/2)):
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")