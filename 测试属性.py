
# 跨模块测试公有属性
# import 第五天面向对象
# print(第五天面向对象.a)   # 跨模块访问属性


# from 第五天面向对象 import *
# print(第五天面向对象.a)



# 跨模块测试受保护属性
# import 第五天面向对象
# print(第五天面向对象._b)   # 跨模块访问属性

# from 第五天面向对象 import *
# print(第五天面向对象._b)




# 私有化属性的应用场景
class  Person(): 
    # 作用：当我们初始化创建好一个实例对象，会自动的调用这个方法初始化
    # def __init__(self):
    #     self.age = 10    #实例属性
    def __init__(self) -> None:
        self.__age = 10
    
    def setAge(self,value):  # 给私有属性设值
        self.__age = value
    
    def getAge(self):       # 获取私有属性
        return self.__age
    
a = Person()   #初始化一个对象  直接初始化了age属性
print(a.age)