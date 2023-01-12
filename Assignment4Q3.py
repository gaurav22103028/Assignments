import random
i=0
while i<10 :
    a=random.randint(0,9)
    b=random.randint(0,9)
    print("Question {}: {} x {} = ".format(i+1, a, b), end="")
    ans=int(input())
    if(ans==(a*b)):
        print("Right!")
    else :
        print("Wrong. The answer is ", a*b)
    i=i+1    
