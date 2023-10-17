import re
print("请输入身份证号：")
text = input()

m = re.match("(^\d{15}$)|(^\d{17}([0-9]|x)$)",text)
if m:
    print (m.group(0))
else :
    print("not match")