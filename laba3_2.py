from math import*
m=[]
for x in range(10, 121, 5):
    y=(3**asin((x/100)/2))+log((2*(x/100)), 3)
    m.append(y)
print(m)
    