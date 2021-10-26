'''
编程：
1、思想--逻辑细想
2、函数
3、数据结构
4、算法
注意：
python中没有do...while循环
'''

'''
迭代器    是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器有两个基本的方法：iter() 和 next()。
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
'''

'''  面向对象
类(Class):  用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：      类中定义的函数。
类变量：    类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：  类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：  如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：  定义在方法中的变量，只作用于当前实例的类。
实例变量：  在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
继承：      即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：    创建一个类的实例，类的具体对象。
对象：      通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。


1、类定义  实例化后可以使用其属性  通过类名访问
2、类对象  属性引用和实例化

类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
'''
'''

class FirstClass:   # 类
    # 属性
    name = ''
    age = 0
    # 方法
    def Self_Class(self):  
        return "FirstClass的方法"
    # def __init__(self,one,two):
    #     self.a = one
    #     self.b = two
    #     print(self.a + self.b)
    
    def addc(a,b):
        print(a+b)
     
# 类的实例化
# x = FirstClass()

# print("FirstClass 类的属性为：",x.i)
# print("FirstClass 类的方法为：",x.Self_Class())

c = FirstClass.addc(1,3)   #调用类中的方法 可以使用类名.方法名(参数)

'''

'''继承
子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。

'''

'''
#定义people大类
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0    #体重
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

#单继承 父类people
class student(people):
     # 子类单独增加属性  年级
    grade = ''  
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

#另一个类，多重继承之前的准备
class speaker():
    # 类 speaker()的属性
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

#多重继承 speaker   student两个类 
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

s = sample('liu',24,90,9,'Python')   #实例化一个例子
s.speak()

'''

# 方法重写  super() 函数是用于调用父类(超类)的一个方法。



# class Parent:        # 定义父类
#    def myMethod(self):
#       print ('调用父类方法')
 
# class Child(Parent): # 定义子类
#    def myMethod(self):
#       print ('调用子类方法')
 
# c = Child()          # 子类实例
# c.myMethod()         # 子类调用重写方法
# super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
'''输出结果
调用子类方法
调用父类方法
'''
# 实例不能访问私有变量  外部不能调用私有方法

# 运算符重载
'''
Python3 中类的静态方法、普通方法、类方法、私有方法

静态方法: 用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，
可以直接使用类名调用。不能和其他方法重名，不然会相互覆盖，后面定义的会覆盖前面的

普通方法: 默认有个self参数，且只能被对象调用。

类方法: 默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器。
不能和其他方法重名，不然会相互覆盖，后面定义的会覆盖前面的

私有方法：两个下划线开头，只能在类内部访问


'''

'''
class Classname:
    @staticmethod
    def fun():
        print('静态方法,可以不带参数')

    @classmethod
    def a(cls):
        print('类方法')

    # 普通方法
    def b(self):
        print('普通方法')

Classname.fun()
Classname.a()
# Classname.b()    #报错
# 普通方法必须实例化对象后才可以调用类的普通方法
c = Classname()
c.b()   
'''

# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
# def printme(age,name):
#     print(name)
#     print(age)

# # 函数中的参数,在调用时，只要规定好，就没有顺序要求
# printme(name ='liu',age = 15)

# printme(age = 15,name = 'liu')

# 不定长参数  所有没有被定义的都会被放进最后的不定长参数里  *+参数名
# 而且是以元组的形式输出，也可以将不定长参数逐个输出

# def printinfo(arg1,*vartuple):
#     print(arg1)
#     print(vartuple)

# printinfo(10,20,30,40)
'''输出
10
(20, 30, 40)
'''
# def printinfo1(arg1,*vartuple):
#     print(arg1)
#     for var in vartuple:
#         print(var)

# printinfo1(10,20,30,40)
'''输出
10
20
30
40
'''

# 不定长参数  一个*是元组的形式   两个**则是字典的形式
# def printinfo2(arg1,**vartuple):
#     print(arg1)
#     print(vartuple)

# printinfo2(10,a = 20,b = 30,c = 40)
'''输出
10
{'a': 20, 'b': 30, 'c': 40}
'''

# 如果  如果参数单独出现*   则*后的参数必须以关键字的形式出现
# def add1(a,b,*,c,d):
#     return a+b+c+d
# # add1(1,2,3,4)    #报错  因为*之前只有两个参数可变
# add1(1,2,c=3,d=4)   #不报错

# 匿名函数   不用def创建   仅仅使用lambda 后接一个表达式
# 格式：    函数名 = lambda 参数  ： 逻辑
# sum = lambda a,b:a+b

# sum(1,2)

# max1 = lambda a,b,c,d: max(a,b,c,d)

# max(10,2,3,4)



'''
python数据结构
列表可以当堆栈   list.append()  list.pop()
列表可以当队列   
'''
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.appendleft("左liu")   #在队列左侧加入新元素
# print(queue)
# queue.append("右liu")   # append()方法默认右侧加入新元素
# print(queue)
# queue.popleft()  #左侧弹出一个元素
# print(queue)
# queue.pop()      #pop()默认右侧弹出
# print(queue)

# 两个序列逐位相乘
# vec1 = [2, 4, 6]
# vec2 = [4, 3, -9]
# # [x*y for x in vec1 for y in vec2]

# [x*y for x in vec1 if x > 3 for y in vec2 if y > 0]   # 可以简单的设计过滤器

# 有关字典中的遍历技巧  使用函数items()同时解读出关键字和对应的值
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k,v in knights.items():
#     print(k,v)

# # 有关序列中的遍历  可以使用enumerate()函数得到索引位置和对应的值
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# 同时遍历多个序列  使用zip()组合
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q,a in zip(questions,answers):
#      print('What is your {0}?  It is {1}.'.format(q, a))

#  如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

'''
输入与输出
Python两种输出值的方式: 表达式语句和 print() 函数。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
'''
# str.format() 的基本使用如下:
# {}里的内容会被format中的参数替换掉  会有顺序可言
# print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# print('{0}网址： "{1}!"'.format('菜鸟教程', 'www.runoob.com'))
# print('{1}网址： "{0}!"'.format('菜鸟教程', 'www.runoob.com'))
'''
菜鸟教程网址： "www.runoob.com!"
菜鸟教程网址： "www.runoob.com!"
www.runoob.com网址： "菜鸟教程!"
'''
# print('{name}网址： "{sites}!"'.format(name='菜鸟教程', sites='www.runoob.com'))
# # 菜鸟教程网址： "www.runoob.com!"
# print('{name}网址： "{sites}!"'.format( sites='www.runoob.com',name='菜鸟教程'))
# # 菜鸟教程网址： "www.runoob.com!"







