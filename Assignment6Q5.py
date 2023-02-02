def funct(lis):
    lis.sort()
    l = len(lis)
    for i in range(l - 1):
        print(lis[i], end="-")
    print(lis[l - 1])
lis=list(map(str,input("Enter the string:").split("-")))
funct(lis)
