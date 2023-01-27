def prime_or_not(k):
    if(k==2):
        print(k,end=",")
    elif(k==1):
        pass
    else:
        for i in range(2,k):
            if(k%i==0):
                break
            if(i==k-1):
                print(k,end=",")

a,b = input("Enter the range seperated by comma:").split(",")
a=int(a)
b=int(b)
for i in range(a,b+1):
    prime_or_not(i)
