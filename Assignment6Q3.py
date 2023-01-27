def factorial(a):
    if(a==0):
        return(1)
    produc=1
    for i in range(1,a+1):
        produc=produc*i
    return(produc)
def nCr(n,r):
    val=factorial(n)/(factorial(r)*factorial(n-r))
    val=int(val)
    return(val)
n=int(input("Enter number of rows:"))
for i in range(n):
    for j in range(i+1):
        print(nCr(i,j),end=" ")
    print("")