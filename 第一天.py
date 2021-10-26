'''
Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

转义字符  \  
如果不想转义就在前面加 r

'''
# print("VSCode\n for python") 
# # VSCode
# # for python
# print(r"vs\ncode")
# # vs\ncode


'''
列表  []  逗号隔开 元素可变      列表截取语法格式：   变量[头下表：尾下表:步进]
'''
# a = [1,3,4,6,7,8]
# a[1:3]  
# # [3,4]
# a[1:-1:2]
# # [3,6]
# a[2] = 0   #列表元素可变
# print(a)

# 字符串的反转
'''

def reversword(input):
    # 使用空格将字符串分隔，把各个单词分隔为列表
    inputwords = input.split(" ")
    # 第一个参数-1表示最后一个元素 第二个参数为空表示移动到末尾  第三个参数-1表示逆向
    inputwords = inputwords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputwords)

    return output

if __name__ == "__main__":
    input = "i love python"
    rw = reversword(input)
    print(rw)

'''

'''
元组 ()   逗号隔开   元素类型可以不同
可以索引  从0开始 -1结束
可以截取  
元素不能修改  

非要修改的话，就切割元组再组合


'''


tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2,[1,2,3] )


'''
集合 set  {}或者set()   创建空集合  必须使用set()
结合可以进行运算  差集(-)  并集(+)  交集(&)  以及都不存在(^)
'''
# # 构建一个集合
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

# print(sites)   # 输出集合，重复的元素被自动去掉

# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')


'''
字典   内置数据类型  {key:value}。
在同一个字典中，键(key)必须是唯一的。
构造函数 dict() 可以直接从键值对序列中构建字典。
'''
# dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])

'''
Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

转义字符  \  
如果不想转义就在前面加 r

'''
# print("VSCode\n for python") 
# # VSCode
# # for python
# print(r"vs\ncode")
# # vs\ncode


'''
列表  []  逗号隔开 元素可变      列表截取语法格式：   变量[头下表：尾下表:步进]
'''
# a = [1,3,4,6,7,8]
# a[1:3]  
# # [3,4]
# a[1:-1:2]
# # [3,6]
# a[2] = 0   #列表元素可变
# print(a)

# 字符串的反转
'''

def reversword(input):
    # 使用空格将字符串分隔，把各个单词分隔为列表
    inputwords = input.split(" ")
    # 第一个参数-1表示最后一个元素 第二个参数为空表示移动到末尾  第三个参数-1表示逆向
    inputwords = inputwords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputwords)

    return output

if __name__ == "__main__":
    input = "i love python"
    rw = reversword(input)
    print(rw)

'''

'''
元组 ()   逗号隔开   元素类型可以不同
可以索引  从0开始 -1结束
可以截取  
元素不能修改  

非要修改的话，就切割元组再组合


'''
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2,[1,2,3] )


'''
集合 set  {}或者set()   创建空集合  必须使用set()
结合可以进行运算  差集(-)  并集(+)  交集(&)  以及都不存在(^)
'''
# # 构建一个集合
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

# print(sites)   # 输出集合，重复的元素被自动去掉

# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')


'''
字典   内置数据类型  {key:value}。
在同一个字典中，键(key)必须是唯一的。
构造函数 dict() 可以直接从键值对序列中构建字典。
'''
# dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# # %%
'''
Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

转义字符  \  
如果不想转义就在前面加 r

'''
# print("VSCode\n for python") 
# # VSCode
# # for python
# print(r"vs\ncode")
# # vs\ncode


'''
列表  []  逗号隔开 元素可变      列表截取语法格式：   变量[头下表：尾下表:步进]
'''
# a = [1,3,4,6,7,8]
# a[1:3]  
# # [3,4]
# a[1:-1:2]
# # [3,6]
# a[2] = 0   #列表元素可变
# print(a)

# 字符串的反转
'''

def reversword(input):
    # 使用空格将字符串分隔，把各个单词分隔为列表
    inputwords = input.split(" ")
    # 第一个参数-1表示最后一个元素 第二个参数为空表示移动到末尾  第三个参数-1表示逆向
    inputwords = inputwords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputwords)

    return output

if __name__ == "__main__":
    input = "i love python"
    rw = reversword(input)
    print(rw)

'''

'''
元组 ()   逗号隔开   元素类型可以不同
可以索引  从0开始 -1结束
可以截取  
元素不能修改  

非要修改的话，就切割元组再组合


'''
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2,[1,2,3] )


'''
集合 set  {}或者set()   创建空集合  必须使用set()
结合可以进行运算  差集(-)  并集(+)  交集(&)  以及都不存在(^)
'''
# # 构建一个集合
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

# print(sites)   # 输出集合，重复的元素被自动去掉

# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')


'''
字典   内置数据类型  {key:value}。
在同一个字典中，键(key)必须是唯一的。
构造函数 dict() 可以直接从键值对序列中构建字典。
'''
# dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])# %%
'''
Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

转义字符  \  
如果不想转义就在前面加 r

'''
# print("VSCode\n for python") 
# # VSCode
# # for python
# print(r"vs\ncode")
# # vs\ncode


'''
列表  []  逗号隔开 元素可变      列表截取语法格式：   变量[头下表：尾下表:步进]
'''
# a = [1,3,4,6,7,8]
# a[1:3]  
# # [3,4]
# a[1:-1:2]
# # [3,6]
# a[2] = 0   #列表元素可变
# print(a)

# 字符串的反转
'''

def reversword(input):
    # 使用空格将字符串分隔，把各个单词分隔为列表
    inputwords = input.split(" ")
    # 第一个参数-1表示最后一个元素 第二个参数为空表示移动到末尾  第三个参数-1表示逆向
    inputwords = inputwords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputwords)

    return output

if __name__ == "__main__":
    input = "i love python"
    rw = reversword(input)
    print(rw)

'''

'''
元组 ()   逗号隔开   元素类型可以不同
可以索引  从0开始 -1结束
可以截取  
元素不能修改  

非要修改的话，就切割元组再组合


'''
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2,[1,2,3] )


'''
集合 set  {}或者set()   创建空集合  必须使用set()
结合可以进行运算  差集(-)  并集(+)  交集(&)  以及都不存在(^)
'''
# # 构建一个集合
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

# print(sites)   # 输出集合，重复的元素被自动去掉

# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')


'''
字典   内置数据类型  {key:value}。
在同一个字典中，键(key)必须是唯一的。
构造函数 dict() 可以直接从键值对序列中构建字典。
'''
# dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])

# %%
'''
Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

转义字符  \  
如果不想转义就在前面加 r

'''
# print("VSCode\n for python") 
# # VSCode
# # for python
# print(r"vs\ncode")
# # vs\ncode


'''
列表  []  逗号隔开 元素可变      列表截取语法格式：   变量[头下表：尾下表:步进]
'''
# a = [1,3,4,6,7,8]
# a[1:3]  
# # [3,4]
# a[1:-1:2]
# # [3,6]
# a[2] = 0   #列表元素可变
# print(a)

# 列表字符串的反转
'''

def reversword(input):
    # 使用空格将字符串分隔，把各个单词分隔为列表
    inputwords = input.split(" ")
    # 第一个参数-1表示最后一个元素 第二个参数为空表示移动到末尾  第三个参数-1表示逆向
    inputwords = inputwords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputwords)

    return output

if __name__ == "__main__":
    input = "i love python"
    rw = reversword(input)
    print(rw)

'''

'''
元组 ()   逗号隔开   元素类型可以不同
可以索引  从0开始 -1结束
可以截取  
元素不能修改  

非要修改的话，就切割元组再组合

'''
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2,[1,2,3] )

# tup1 = (20)
# print(type(tup1))   #class int
# # 唯一的区别就是是否带 ,   前提条件是元组中只有一个元素
# tup2 = (20,)
# print(type(tup2))   #class tuple



# # 元组的修改
# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
 
# # 以下修改元组元素操作是非法的。
# # tup1[0] = 100
 
# # 创建一个新的元组
# tup3 = tup1 + tup2
# print (tup3)




'''
集合 set  {}或者set()   创建空集合  必须使用set()
结合可以进行运算  差集(-)  并集(+)  交集(&)  以及都不存在(^)
'''
# # 构建一个集合
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

# print(sites)   # 输出集合，重复的元素被自动去掉

# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')


'''
字典   内置数据类型  {key:value}。
在同一个字典中，键(key)必须是唯一的。
构造函数 dict() 可以直接从键值对序列中构建字典。
字典的内置函数：
clear() keys() values()

'''
# a = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# {'Runoob':1,'Google':2,'Taobao':3}


# 字典遍历--方法一

# def example(d):
#     for c in d:
#         print(c)  #输出单个的键
#         print(c,':',d[c])   #输出键值对

# example(a)   # 输出 Runoob Google  Taobao


'''
比较运算符：
==   比较对象是否相等
!=   比较两个对象是否不相等
>    返回x是否大于y
<    返回x是否小于y
<=   返回x是否大于等于y。
>=   返回x是否小于等于y。

赋值运算符：
=	简单的赋值运算符	  c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	      c += a 等效于 c = c + a
-=	减法赋值运算符	      c -= a 等效于 c = c - a
*=	乘法赋值运算符	      c *= a 等效于 c = c * a
/=	除法赋值运算符	      c /= a 等效于 c = c / a
%=	取模赋值运算符	      c %= a 等效于 c = c % a
**=	幂赋值运算符	      c **= a 等效于 c = c ** a
//=	取整除赋值运算符	  c //= a 等效于 c = c // a


位运算符：
a = 0011 1100    b = 0000 1101
&	按位与运算符：有0则为0 	(a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：有1则为1	(a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：相同为0 相异为1 	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111

成员运算符：
in  如果在指定的序列中找到值返回 True，否则返回 False。
not in  如果在指定的序列中没有找到值返回 True，否则返回 False。

'''
# a = 10
# b = 2
# list = [1,3,20,3]

# if (a in list):
#     print('a in list!')
# else:
#     print('a not in list!')

# if (b in list):
#     print('b in list!')
# else :
#     print('b not in list')



'''
变量在使用前必须定义==赋值  否则会认为是错误  

'''

# name = "liuchenxu"
# f'hello {name}'    #这里将name替换成liuchenxu  使用f不再考虑name的类型  不过这里要注意的是'{}'




'''
字典   可变容器  可存储任意类型的对象
键必须唯一   值不用唯一 可以是标准的对象 也可以是用户自定义的 {key:value,key:vlaue}
访问值，寻找对应的键就行

字典内置方法：
	radiansdict.clear()  删除字典内所有元素

'''

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# # print("dict['Name']:",dict['Name'])
# # dict['Name']:Runoob
# dict['Name'] = 'Taobao'   #修改键的值
# print("dict['Name']:",dict['Name'])
# # dict['Name']:Taobao

# print(len(dict))
# print(str(dict))
# type(dict)

# 字典习题1
# x = True
# country_counter = {}

# def addone(country):
#     if country in country_counter:
#         country_counter[country] += 1
#     else:
#         country_counter[country] = 1

# addone('China')
# addone('Japan')
# addone('china')

# print(country_counter)
# print(len(country_counter))

# 习题2
# confusion = {}
# confusion[1] = 1
# confusion['1'] = 2
# confusion[1] += 1

# sum = 0
# for k in confusion:
#     sum += confusion[k]

# print(confusion)
# print(sum)

# 字典的无限嵌套
# cities={
#     '北京':{
#         '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
#         '海淀':['圆明园','苏州街','中关村','北京大学'],
#         '昌平':['沙河','南口','小汤山',],
#         '怀柔':['桃花','梅花','大山'],
#         '密云':['密云A','密云B','密云C']
#     },
#     '河北':{
#         '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
#         '张家口':['张家口A','张家口B','张家口C'],
#         '承德':['承德A','承德B','承德C','承德D']
#     }
# }
# for i in cities['北京']:    #键中键
#     print(i)
# print('\n')
# for i in cities['北京']['朝阳']:
#     print(i)


'''
一个比较好用的用户决定循环结束的例子：
write = 1
while write:
    一系列重复性的操作
    write = int(input('继续输入？\n 1/继续  0/退出'))
如果输入1  继续while循环中的操作
如果输入0  执行while循环后的操作
'''

# 集合  就类似数学中的集合  去重  交 并 差等
'''
add()	                为集合添加元素
clear()	                移除集合中的所有元素
copy()	                拷贝一个集合
difference()	        返回多个集合的差集
difference_update()	    移除集合中的元素，该元素在指定的集合也存在。
discard()	            删除集合中指定的元素
intersection()	        返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	        判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	            判断指定集合是否为该方法参数集合的子集。
issuperset()	        判断该方法的参数集合是否为指定集合的子集
pop()	                随机移除元素
remove()	            移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	                返回两个集合的并集
update()	            给集合添加元素
'''


