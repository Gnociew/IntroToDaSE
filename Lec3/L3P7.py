print("请输入两个整数")
x = int(input())

num = x
y = int(input())

if y < x :
    num = y

while num >= 1 :
    if x%num == 0 and y%num == 0 :
        re = num
        break
    else :
        num-=1

print("%d和%d的最大公约数是%d"%(x,y,num))
