print("请输出您的成绩：")
x = input()
x = int(x)

if x < 60 :
    print("您的等级为不合格")
elif x>= 60 and x < 75 :
    print("您的等级为合格")
elif x >= 75 and x <90 :
    print("您的等级为良好")
else :
    print("您的等级为优秀")