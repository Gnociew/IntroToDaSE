#选择排序
def SelectSort(list):
    length = len(list)
    
    if length <= 1:
        return list
    
    for i in range(length):
        min = i
        for j in range(i+1,length):
            if list[j] <list[i]:
                min = j
        if min != i :
            temp = list[i]
            list[i] = list[min]
            list[min] = temp
    
    return list

#冒泡排序
def BubbleSort(list):
    length = len(list)
    
    if length <= 1:
        return list
    
    for i in range(1,length):
        for j in range(0,length-i):
            if list[j] > list [j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    
    return list

#归并排序
def merge(lList,rList):
    newList = []
    l = r = 0
    while l < len(lList) and r < len(rList):
        if lList[l] < rList[r]:
            newList.append(lList[l])
            l += 1
        else:
            newList.append(rList[r])
            r += 1
        
    if l == len(lList):
        for i in rList[r:]:
            newList.append(i)
    else:
        for i in lList[l:]:
            newList.append(i)
    return newList

def MergeSort(list):
    length = len(list)

    if length <= 1:
        return list
    
    mid = length // 2
    left = MergeSort(list[:mid])
    right = MergeSort(list[mid:])
    
    return merge(left,right)

#快速排序
def partition(list,l,r):
    p = list[r]
    i = l-1

    for j in range(l,r):
        if list[j] <= p:
            i += 1
            list[i],list[j] = list[j],list[i]
        
    list[i+1],list[r] = list[r],list[i+1]
    return i+1

def QuickSort(list,l,r):
    length = len(list)
    
    if length <= 1:
        return list
    
    flag = partition(list,l,r)
    QuickSort(list,l,flag-1)
    QuickSort(flag+1,list)

list = [4,2,5,33,25,6,4,2,4]
print(MergeSort(list))