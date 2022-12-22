side_a = int(input('Enter length of side a: '))
side_b = int(input('Enter length of side b: '))
side_c = int(input('Enter length of side c: '))
if(side_a+side_b>side_c and side_b+side_c>side_a and side_c+side_a>side_b):
    print("Yes")
else:
    print("No")