n = int(input("Enter number of rows:"))
a=65
for i in range(n):
    for j in range(i+1):
        print(chr(a),end="")
        a=a+1
    print("")