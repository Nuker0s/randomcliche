import math
import random

m1=[]
m2=[]

for x in range(0,3):
    m1.append([])
    for y in range(3):
        m1[x].append(random.randint(0,3))
for x in m1:
    print(x)
print("-------")
for x in range(0,3):
    m2.append([])
    for y in range(3):
        m2[x].append(random.randint(0,3))
for x in m2:
    print(x)


