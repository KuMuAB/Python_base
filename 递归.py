# # 斐波那契函数
# def func1(x):
#     if x == 1 or x == 2:
#         return 1
#     else:
#         return func1(x-1) + func1(x-2)

# print (func1(5))

# # 汉诺塔问题    从哪个柱子经过哪个柱子到哪个柱子
# def HanNuota(n,a,b,c):  # n个盘子  从a经过b到c
#     if n > 0:
#         HanNuota(n-1,a,c,b)
#         print('moving from %s to %s'%(a,c))
#         HanNuota(n-1,b,a,c)
# HanNuota(2,'A','B','C')

'''
# 列表查找  index()
def linear_search(li,val):
    for ind,v in enumerate(li):
        if v == val:
            return ind
    else:
        return None

# 二分查找
def binary_search(li,val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return None

 
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
           
binary_search(list,6)
linear_search(list,4)
'''

'''
# 列表排序   sort()
import random
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False  #加一个标记位来判断是否进行冒泡
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        print('第%d趟'%i,li)
        if not exchange:  #如过一趟下来没有冒泡 说明已经排好序
            return 

li = [9,8,7,1,2,3,4,5]
bubble_sort(li)
'''

'''
# 选择排序
def select_sort_simple(li):
    li_new = []  #创建新列表进行排序
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)  # 删除最下值 不删除的话 一直反馈这个最小值
    return li_new


def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
                exchange = True
        li[i],li[min_loc] = li[min_loc],li[i]
        print(li)

li = [1,2,3,5,6,7,75,43,9]
select_sort(li)
print(li)
'''

'''
# 插入排序
def insert_sort(li):
    for i in range(1,len(li)):
        tem = li[i]
        j = i - 1  # 手里的牌的下标
        while j >= 0 and li[j] > tem: # 找插入的位置
            li[j + 1] = li[j]
            j -= 1
        li[j+1] = tem
        print(li)

li = [9,8,7,1,2,3,4,5]
insert_sort(li)
print(li)
'''


'''
# 快速排序

def partition(li,left,right):
    tmp = li[left]    # 保存最左侧的数
    while left < right:
        while left < right and li[right] >= tmp:  #从右面找比tmp小的数
            right -= 1  #往左走一步
        li[left] = li[right]  #把右边的值写到左边空位上
        while left < right and li[left] <= li[right]:
            left += 1  #往右走一步
        li[right] = li[left]   #把左边的值写到右边空位上
    li[left] = tmp    #tmp归位
    return left

def quick_sort(data,left,right):
    if left < right: #至少两个元素
        mid = partition(data,left,right)
        quick_sort(data,mid+1,right)
        quick_sort(data,left,mid-1)


li = [9,8,7,1,2,3,4,5]
quick_sort(li,0,len(li)-1)
print(li)
'''