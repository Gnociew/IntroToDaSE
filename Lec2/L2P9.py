import numpy as np
import random

count = 0
for i in range(0,100000):
    x = random.uniform(2,3)
    y = random.uniform(0,21)
    if y <= x**2 + 4*x*np.sin(x) :
        count+=1
p = count / 100000
s = p*21
print("%.5f"%s)