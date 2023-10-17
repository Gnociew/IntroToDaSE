#定义节点类
class Node(object):
    def __init__(self,data,next = None):
        self.item = data
        self.next = next

# 定义单链表类
class LinkList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
        #如果空返回True 非空返回False
    
    #头插法
    def add(self,item):
        node = Node(item)
        node.next = self.head
        self.head = node
    
    #尾插法
    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            temp = self.head
            while temp.next != None :
                temp = temp.next
            temp.next = node
        
    def delect(self,item):
        temp = self.head
        prev = None
        while temp != None:
            if temp.item == item :
                if prev == None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return True
            else:
                prev = temp
                temp = temp.next
        return False
    
    def search(self,item):
        temp = self.head
        while temp != None:
            if temp.item == item:
                return True
            else:
                temp = temp.next
        return False
    
    def replace(self,item,New_item):
        temp = self.head
        while temp != None:
            if temp.item == item:
                temp.item = New_item
                return True
            else:
                temp = temp.next
        return False
    
if __name__ == '__main__':
    link_list = LinkList()

    for i in range(5):
        link_list.append(i)
    
    link_list.add(6)

    link_list.delect(4)

    r = link_list.search(1)
    print(r)

    link_list.replace(2,3)
