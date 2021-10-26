'''
class Person(object):
    name = None
    age = None

    def run(self):
        print(f'{self.name}在奔跑,{self.age}岁了')
    
    def jump(self):
        print(f'{self.name}在跳跃')

    def work(self):
        self.run()
        self.jump()
    
 

xiaomu = Person()       #实例化一个对象
xiaomu.name = "小牧"    # 类变量赋值
xiaomu.age = 12
xiaomu.work()           #调用类方法

# 实例化对象不通用类的方法

'''

'''
# 构造函数
class Gouzao():   #创建类
    # 构造函数
    def __init__(self,a,b):
        self.a = a
        self.b = b
    # 类的方法
    def run(self):
        print(self.a,self.b)

G = Gouzao(4,5)   #传参到 a b 

G.run()
'''


'''
#  私有函数   私有变量   __开头的就是私有的
class Private():
    __cat_name = "私有变量"
    cat_name = "公有变量"
    def run(self):                  #公有方法
        print('这是公有方法')
        print(f'{self.cat_name}   hhhh')
        self.__run()                #在公有方法中调用私有方法
    
    def __run(self):                #私有方法
        print(f'{self.__cat_name}  hhhh')
        print('这是私有方法')

Cat = Private()
# print(Cat.__cat_name)    #报错，无法访问私有变量
print(Cat.cat_name)
Cat.run()
# Cat.__run()   #报错，无法访问私有函数
'''

'''
# python的封装

class Parent(object):
    def __hello(self,data):
        self.data = data
        print('hello %s '% data)
    def hello(self):    #通过公有函数调用私有函数
        self.__hello('python')

p = Parent()
p.hello()
'''


# # 装饰器   使用函数
# def outfun(func_args):    #外围函数
#     def interfun(*args,**kwargs):   #内嵌函数，参数是不定长的，**则通过字典的形式
#         return func_args(*args,**kwargs)
#     return interfun   #外围函数中返回内嵌函数


'''
def check_str(func):
    print(check_str)
    def inter(*args,**kwargs):
        result = func(*args,**kwargs)
        print(args,kwargs)
        if result == 'ok':
            return 'result is %s' % result
        else:
            return 'result is failed: %s' % result
    return inter    #返回内部函数一定不能忘

@check_str   #引用装饰器    等同于 test = check_str(test)
def test(data):
    return data 

result = test(data = 'no')
print(result)
result = test(data= 'ok')
print(result)
'''
# classmethod 装饰器的用法

# class Test(object):
#     @classmethod
#     def func(cls,a,b):
#         print('这是测试装饰器的！ ')
#         return a + b
# # 这里没有经过实例化便直接调用func函数
# Test.func(3,4)   


'''

class Person:
    # 限制实例化对象无限制添加属性
    __slots__ = ["age"]    #这里意思是后续实例化对象只能添加age属性
    # 凡是通过Person类创建的对象都无法增加其他属性
    pass

# 此时p对象是没有age这个属性的
p = Person()


p.age = 10
p.name = 11
print(p.age)
print(p.name)   #  这句话报错，因为类中限制了只能添加age属性

'''

'''
class Person:
    age = 10
    pass

p = Person()
# 这句代码  是p对象的新增age属性
p.age += 5
# 等同于这句代码    等号右边是访问对象中的age，但是此时对象中没有
# 所以访问到类中的age，此时age是10
# 等号左边此时是给p对象新增age
p.age = p.age + 5

print(Person.age)  # 这里访问的是类中的age 所以输出10
print(p.age)       # 这里访问的是对象p中新增的age属性，所以输出15
'''

'''
class Person:
    pass

p = Person()
# # 增加属性
# p.age = 18
# p.height = 88
# p.name = "liu"

# print(p.__dict__)    #查看对象的所有属性
# # 给Person类添加属性
'''

'''
# 方法的规划依据：第一个参数接收的数据类型   
# 实例方法(第一个参数是实例) 类方法(第一个参数是类)  静态方法

class Person:
    def eat(self):  #self只是一个形参，接收的是一个实例
        print("这是一个实例方法",self)
        # 这是一个实例方法 <__main__.Person object at 0x0000020B2EE67970>
    @classmethod
    def leimethod(cls):  #接收的是一个类
        print("这是一个类方法",cls)
        #输出： 这是一个类方法 <class '__main__.Person'>
    
    @staticmethod
    def jingtaimethod():
        print("这是一个静态方法")

# 实例化一个对象
p = Person()
p.eat()

# Person.eat()   # 会报错

Person.leimethod()


print(p.__dict__)  # 输出的是字典
print(Person.__dict__)
'''
'''
class Person:
    age = 0   # 类属性

p = Person()
p.num = 9     # 实例属性

print(Person.age)       
print(p.age)

# print(Person.num)   #  这句话报错
print(p.num)
'''

# # 给类加注释
# class Person:
#     '''
#     在这里加类的注释，方便后续的阅读
#     '''
#     # 在代码句的上方添加注释
#     count = 1

#     def run(self):
#         '''
#         在这里给函数/方法的作用或者达到的效果做备注/解释
#         '''
#         print("跑起来！")

# help(Person)

# 相关属性
'''
1、私有属性   保证数据的安全性
    仅仅类内部访问
2、只读属性
3、内置特殊属性



z   公有属性
        类内部
        子类内部
        模块内其他位置
        跨模块访问
            import形式导入
            from 模块 import *
_x  受保护的属性
        类内部
        子类内部
        模块内其他位置
__y  私有属性
        类内部
    应用：
        数据保护
        数据过滤
'''

'''
class Animal:
    # 类的内部
    name = "公有的"    # 公有属性
    __wife = "私有的"   # 私有属性
    _money = "受保护的"  # 保护属性
    def PName(self):
        # print(Animal.name)    #类内部访问公有属性
        # print(self.name)      #类内部访问公有属性

        # print(self._money)      #类内部访问受保护属性 
        # print(Animal._money)    #类内部访问受保护属性 

        print(self.__wife)      #类内部访问私有属性 
        print(Animal.__wife)    #类内部访问私有属性 
    pass

# a = Animal()
# a.PName()


class Dog(Animal):    # 继承自Animal
    # Animal 类的外部  Dog类(子类)的内部
    def PName2(self): 
        # print(Dog.name)    #子类内部访问父类中的公有属性
        # print(Dog._money)    #子类内部访问父类中的受保护属性
        print(Dog.__wife)
    pass

# d = Dog()
# d.PName2()

# a = 234    #测试属性文件中的跨模块访问
_b = 123   #用于测试跨模块访问受保护属性


# 其他位置访问受保护属性
# print(Animal._money)
# print(Dog._money)
# print(a._money)
# print(d._money)


# 其他位置访问私有属性
# print(Animal.__wife)
print(Animal._Animal__wife)    #这种方式可以访问私有属性--解释器
# print(Dog.__wife)
# print(a.__wife)
# print(d.__wife)

'''

