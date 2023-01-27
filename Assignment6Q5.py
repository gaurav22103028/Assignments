lis=list(map(str,input("Enter the string:").split("-")))
lis.sort()
l=len(lis)
for i in range(l-1):
    print(lis[i],end="-")
print(lis[l-1])