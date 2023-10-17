import random

n = 20
listA = []
listB = []

for i in range(0,n):
    listA.append(random.randint(0,10))

for i in range(0,n):
    num = 1
    for k in range(0,n):
        if(k != i):
            num = num * listA[k]
    listB.append(num)

print(listA)
print(listB)