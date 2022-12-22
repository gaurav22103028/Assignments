def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b
nterms = int (input("How many Terms of the Fibonacci series? "))
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    sum = 0
for i in range(nterms):
    cnumber=fibonacci(i)
    sum = sum + cnumber
    print(cnumber)
print("Average is : ", sum/nterms)