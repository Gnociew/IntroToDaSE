x = input()
x = float(x)

list = []
while x != 0 :
    x = x*2
    if x < 1 :
        list.append(0)
    else :
        list.append(1)
        x = x-1

print("0.",end="")
for i in list:
    print(i,end="")