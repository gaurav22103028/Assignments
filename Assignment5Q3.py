import math

a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
s=(a+b+c)/2
if(((s*(s-a)*(s-b)*(s-c))<=0) or a<0 or b<0 or c<0):
    print("Triangle is not possible")
else:
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(area)