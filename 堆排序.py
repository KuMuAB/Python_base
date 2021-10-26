import random

#  调整函数
def sift(li,low,high):
    #  li：  列表  
    #  low:  堆的根节点位置
    #  high：堆的最后一个元素的位置
    i = low    #  i最开始指向根节点
    j = 2 * i + 1  # j最开始指向左孩子
    tmp = li[low]   # 存取堆定的值
    while j <= high:  # 确定j位置有数
        if j + 1 <= high and li[j+1] > li[j]:  # 如果有右孩子且比较大
            j += 1   # 指向右孩子
        if li[j] > tmp:  
            li[i] = li[j]
            i = j  # 往下走一层
            j = 2 * i + 1
        else:   # tmp大
            li[i] = tmp
            break
    else:
        li[i] = tmp

def topk(li,k):
    heap = li[0:k]  # 取出列表中的前k个值
    for i in range((k - 2)//2,-1,-1):
        sift(heap,i,k-1)
    # 1.建堆
    for i in range(k,len(li) - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap,0,k-1)
    # 2.遍历
    for i in range(k-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        sift(heap,0,i-1)   
    # 3.挨个出数
    return heap


def  heap_sort(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1):   # 通过孩子节点找父节点
        #  i 表示建堆时 调整部分的根的下标
        sift(li,i,n-1)
    # 建堆完成
    for i in range(n-1,-1,-1):
        #  i 指向当前堆的最后一个元素
        li[0],li[i] = li[i],li[0]
        sift(li,0,i-1)    # i-1 是新high

li = [i for i in range(100)]    
random.shuffle(li)
# heap_sort(li)
# print(li)
print(topk(li,10))


# # 使用python的内置包
# import heapq

# li = [i for i in range(100)]    
# random.shuffle(li)  #给一个乱序的数据

# heapq.heapify(li) #建堆
# # print(li)

# n = len(li)
# for i in range(n):
#     print(heapq.heappop(li),end = ",")  # 每次弹出一个最小值



