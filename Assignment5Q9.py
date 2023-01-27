x = [str(x) for x in input("Enter multiple values: ").split()]
diction=dict()
for i in x:
    if i in diction.keys():
        diction[i] = diction[i]+1
        continue
    diction[i]=1
print(diction)