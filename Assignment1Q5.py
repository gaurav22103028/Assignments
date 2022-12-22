import math
s=0
for i in range(24):
    print(i*15, "---", round(math.sin(s), 4), round(math.cos(s), 4))
    s=s+math.pi/12

