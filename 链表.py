class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

# 链表头插法
def creat_linklist_head(li):
    head = Node(li[0])   # 创建头结点
    for element in  li[1:]:
        node = Node(element)
        node.next = head
        head = node 
    return head

# 链表尾插法
def creat_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in  li[1:]:
        node = Node(element)
        tail.next = node
        tail = node 
    return head

#判断链表是否为空
def is_empty(self):
    if self.getlength() ==0:
        return True
    else:
        return False
#  获取链表长度
def getlength(self):
    p =  self.head
    length = 0
    while p!=0:
        length+=1
        p = p.next
    return length


def print_linklist(lk):
    while lk:
        print(lk.item,end = " ")
        lk = lk.next

# lk1 = Node()
lk1 = creat_linklist_tail([1,2,3,6,8,9])  # 尾插法
print_linklist(lk1)
lk2 = creat_linklist_head([3,2,5,6,7])    # 头插法
print('')
print_linklist(lk2)
