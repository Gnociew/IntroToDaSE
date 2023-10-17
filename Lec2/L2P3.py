#0:人狼羊菜
#1：人狼羊
#2：人狼菜
#3：人羊菜
#4：人羊
#5：狼菜
#6：狼
#7：羊
#8：菜
#9：空

def dfs(road,state,s,count):
    if state == 9:
        k = 1
        while s[k] != 0 and k < 10 :
            print(s[k],end=" ")
            k+=1
        print("\n")
        return
        
    for i in range(0,10):
        if road[state][i] :
            count+=1
            #print(count)
            s[count] = i
            dfs(road,i,s,count)
            #count-=1
            #print(count)
            s[count]=0
            count-=1
    return

road = [[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,1],
        [0,0,1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0]]

s = []
for i in range(0,10):
    s.append(0)
count = 0

state = 0

dfs(road,state,s,count)