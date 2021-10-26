import random

# 归并排序
'''

'''
def merge(li,low,mid,high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:  # 循环的条件
        if li[i] < li[j]:
            ltmp.append(li[i])   # 新列表添加小的
            i += 1
        else:
            ltmp.append(li[j])
            j += 1    
    while i <= mid:  #不满足第一个循环后
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp

def merge_sort(li,low,high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li,low,mid)
        merge_sort(li,mid + 1,high)
        merge(li,low,mid,high)

li = [i for i in range(100)]  
random.shuffle(li)
print(li)
merge_sort(li,0,len(li) - 1)
print(li)