n = input()
n = int(n)

list = []
list2 = []
s = []
flag = []
for i in range(0,n+1):
    list.append(0)
    list2.append([])
    s.append(0)
    flag.append(-1)

list[0] = 0
list[1] = 1
max = 0

for i in range(2,n+1) :
    max = 0
    mid = int(i/2)
    for num1 in range(1,mid+1) :
        num2 = i - num1
        if num1 > list[num1] :
            list[num1] = num1
            list2[num1] = [num1]
        if num2 > list[num2] :
            list[num2] = num2
            list2[num2] = [num2]
        re = list[num1] * list[num2]
        if re > max :
            max = re
            p = num1
            q = num2
    list[i] = max
    list2[i] = list2[p] + list2[q]
    s[i] = num1


print(list[n])
print(list2[n])