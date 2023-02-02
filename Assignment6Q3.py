def factorial(a):
    if(a==0):
        return(1)
    produc=1
    for i in range(1,a+1):
        produc=produc*i
    return(produc)

# input for the number of rows
n = int(input("Rows:"))
for i in range(n):
    for j in range(n - i + 1):
        # for left spacing
        print(end=" ")
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    # for new line
    print()
