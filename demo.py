# 代码注释
"""
这是一个多行注释
"""
print("Hello, World!")
print(len("Hello, World!"))
print(len('汉字'))
print(9)
print(9.0)
print(True)
print(None)
print("Hello, World!"[4])
print("Hello, World!"[0:5])

# 数据类型
# 在 Python 中没有double类型，有浮点数（float）类型，其遵循双精度（double）浮点数的标准，通常占用 8 个字节（64 位）
print(type(9))
print(type(9.0))
print(type(9.00))
print(type(True))
print(type(None))

# 数据输入
# user_name = input("请输入您的姓名：")
# user_age = input("请输入您的年龄：")
# print("您的姓名是：" + user_name + "，您的年龄是：" + user_age)
# print("您的姓名是：%s，您的年龄是：%s" % (user_name, user_age))
# print("您的姓名是：{}，您的年龄是：{}".format(user_name, user_age))
# print(f"您的姓名是：{user_name}，您的年龄是：{user_age}")
# print("类型：%s" % type(user_name) + "，类型：%s" % type(user_age))

# 条件语句
# mood_index = int(input("请输入您的心情指数："))
# if mood_index >= 90:
#     print("您的心情很好！")
# elif mood_index >= 60:
#     print("您的心情一般！")
# else:
#     print("您的心情不好！")

# 嵌套条件语句
# score = int(input("请输入您的成绩："))
# if 0<= score <= 100:
#     if score >= 90:
#         print("优秀")
#     elif score >= 80:
#         print("良好")
#     elif score >= 60:
#         print("及格")
#     else:
#         print("不及格")
# else:
#     print("输入错误！")


# 逻辑运算
print(1 == 1)
x = 15
print(x>10 and (x<20 or x==30))
print(not x>10)

# 列表：list 有序、可变、元素可重复
list1 = [1, 2, 3, 4, 5]
list1.append(6)
list1.insert(0, 0)
list1.remove(3)
print(list1) # [0, 1, 2, 4, 5, 6]
print(list1[0]) # 0
print(list1[1:3]) # [1, 2]
print(list1[1:]) # [1, 2, 4, 5, 6]
print(list1[:3]) # [0, 1, 2]
print(list1[-1]) # 6
print(list1[-3:-1]) # [4, 5]
print(list1.index(4)) # 3
print(4 in list1)   # True
print(len(list1))   # 6


# 集合：set 无序、不可重复
print("集合：====================")
set1 = {1, 2, 3, 4, 5}
set1.add(6) # {1, 2, 3, 4, 5, 6}
set1.add(4) # {1, 2, 3, 4, 5, 6}
set1.remove(3) # {1, 2, 4, 5, 6}
print(set1) # {1, 2, 4, 5, 6}
print(4 in set1)
print(len(set1))

# 元组：tuple 有序、不可变、元素可重复
print("元组：====================")
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(tuple1[0])
print(tuple1[1:3]) # (2, 3)
print(tuple1[1:]) # (2, 3, 4, 5)
print(tuple1[:3]) # (1, 2, 3)
print(tuple1[-1]) # 5
print(tuple1[-3:-1]) # (3, 4)
print(tuple1.index(4)) # 3
print(4 in tuple1)
print(len(tuple1))

contacts = {
    ("张三",23): "123456",
    ("李四",26): "654321",
    ("王五",18): "987654"
}
print(contacts[("张三",23)])

# 字典：dict 无序、可变、key不可重复
print("字典：====================")
dict1 = {
    "name": "张三",
    "age": 23,
    "phone": "123456"
}
print(dict1)
print(dict1["name"])
print(dict1["age"])
print("name" in dict1) # True
print("address" in dict1) # False
print("张三" in dict1) # False
dict1["address"] = "北京"
print(dict1)    # {'name': '张三', 'age': 23, 'phone': '123456', 'address': '北京'}
del dict1["phone"]
print(dict1)    # {'name': '张三', 'age': 23, 'address': '北京'}
print(len(dict1))   # 3
print(dict1.keys()) # dict_keys(['name', 'age', 'address'])
print(dict1.values())   # dict_values(['张三', 23, '北京'])
print(dict1.items())    # dict_items([('name', '张三'), ('age', 23), ('address', '北京')])

# for 循环
print("for 循环：====================")
for i in range(5):
    print(i)    # 0 1 2 3 4
print("for 循环 finish1")
for i in range(1, 5):
    print(i)    # 1 2 3 4
print("for 循环 finish2")
for i in range(1, 10, 2):
    print(i)    # 1 3 5 7 9
print("for 循环 finish3")
for i in range(5, 0, -1):
    print(i)    # 5 4 3 2 1
print("for 循环 finish4")

# while 循环
print("while 循环：====================")
i = 0
while i < 5:
    print(i)    # 0 1 2 3 4
    i += 1
print("while 循环 finish")

# 字符串格式化方式
print("字符串格式化方式：====================")
message_content = """
    您好，%s！
    您的年龄是：%d
    您的电话是：%s
"""
print(message_content % ("张三", 23, "123"))
print("您好，{}！\n您的年龄是：{}\n您的电话是：{}".format("李四", 88, "456"))
print("您好，{name}！\n您的年龄是：{age}\n您的电话是：{phone}".format(name="王五", age=65, phone="188"))
message_content = """
    您好，{0}！
    您的名字是：{0}
    您的成绩是：{1:.2f}
"""
print(message_content.format("张三", 23))
name = "赵六"
age = 33
phone = "789"
print(f"您好，{name}！\n您的年龄是：{age}\n您的电话是：{phone}")

# 函数
print("函数：====================")
def say_hello(value):
    print(f"Hello, World! {value**2}")
say_hello(3)

def add(a, b):
    print(f"入参：{a}，{b}")
    return a + b
print(add(3, 4))

def add(a, b=1):
    print(f"入参：{a}，{b}")
    return a + b
print(add(3))
print(add(6, 5))

def add(*args):
    print(args)
    return sum(args)
print(add(1, 2, 3, 4, 5))

def add(**kwargs):
    print(kwargs)
    return sum(kwargs.values())
print(add(a=1, b=2, c=3, d=4, e=5))

# 高阶函数和匿名函数
# 高阶函数：函数接收的参数是一个函数，或者函数的返回值是一个函数
# 匿名函数：没有名字的函数，使用 lambda 关键字定义
print("高阶函数和匿名函数：====================")
def add(a, b, f):
    return f(a) + f(b)
print(add(3, -4, abs))  # 7
print(add(3, 4, lambda x: x**2)) # 25
print("匿名函数：====================")
# 匿名函数也有局限性，冒号后没法有多个语句或表达式，只适用于比较简单的场景
add = lambda a, b: a + b
print(add(3, 4))    # 7
print((lambda a, b, f: f(a) + f(b))(3, 4, lambda x: x**2))  # 25


# 模块导入
print("模块导入：====================")
import math
print(math.pi)
print(math.e)
print(math.sin(math.pi/2))
print(math.cos(math.pi))
print(math.log(10))

from math import pi, e, sin, cos, log
print(pi)
print(e)
print(sin(pi/2))
print(cos(pi))
print(log(10))

from math import *
print(pi)
print(e)
print(sin(pi/2))
print(cos(pi))
print(log(10))

# 三方库导入
# 在终端中使用 pip install 后面加上库的名字 来安装三方库，然后即可导入使用
# import requests
# response = requests.get("http://www.baidu.com")
# print(response.status_code)

# 类
print("类：====================")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Hello, {self.name}!")
    def say_age(self):
        print(f"您的年龄是：{self.age}")
    def say_info(self):
        print(f"您的姓名是：{self.name}，您的年龄是：{self.age}")
person = Person("张三", 23)
person.say_hello()
person.say_age()
person.say_info()

# 继承
print("继承：====================")
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score
    def say_score(self):
        print(f"您的成绩是：{self.score}")
student = Student("李四", 26, 88)
student.say_hello()
student.say_age()
student.say_info()
student.say_score()

# 文件操作
# 第二个参数可以不写，不写时默认为读取模式 ”r”
print("文件操作：====================")
# 文件写入
# 使用w模式打开文件进行写入时，如果文件已存在，将会把原有文件内容全部清空,不存在则创建
file = open("./demo.txt", "w", encoding="utf-8")
file.write("Hello, World!\n")
file.write("啊哈哈")
file.close()
# 文件读取
file = open("./demo.txt", "r", encoding="utf-8")
# 运行read()方法会一次性读取文件里面的所有内容，并以字符串的形式返回
# 运行read()方法后，再次调用时返回的结果为空，因为程序会记录文件读取到哪个位置，
# 第一次运行read()时已经读到结尾，第二次运行时后面已经没有内容
# 文件太大时不建议使用read()方法，因为读出来的内容会占用很大的内存。
# 如果不需要一次性读取整个文件，可以在read()传一个数字，表示读多少个字节，下次调用read时会从上次结束位置继续往下读
# file.read(10)
content = file.read()
print(content)
file.close()

# readline() 方法 文件读取
print("readline() 方法 文件读取：====================")
file = open("./demo.txt", "r", encoding="utf-8")
# readlines()读取所有内容的行列表，一般配合for循环使用
# print(file.readlines())
# 读取一行内容
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
#     如使用 with 方式，不需要手动关闭文件，需要注意代码缩进
file.close()

# open()的第二个参数需要传入附加模式”a”参数，表示追加内容,不存在则创建
print("文件追加：====================")
with open("./demo.txt", "a", encoding="utf-8") as file:
    file.write("\n==这里是追加内容")
    file = open("./demo.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)

#  open()方法的第二个参数传入”r+”参数，就可以同时支持读写文件
print("文件读写：====================")
with open("./demo.txt", "r+", encoding="utf-8", errors="ignore") as file:
    file.seek(60)
    file.write("\n")
    file.write("你好啊！\n")
    file.write("可读写文件")
    file.seek(0)   # seek()方法可以移动文件读取指针到指定位置，0表示文件开头
    content = file.read()
    print(content)

# 异常处理
print("异常处理：====================")
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
except:
    print("未知错误")
else:
    print("没有错误")
finally:
    print("程序执行完毕！")

# 测试 assert断言、unittest 单元测试
# 测试方法命名必须以 test_ 开头。因为 unittest 库只把 test_ 开头的方法当作测试用例
# assert 1 == 1
# assert 1 == 2
# 测试用例编辑完成后，需要在编辑器的【终端】窗口中输入 python -m unittest 运行unittest库，
# 这个库就会自动搜索所有继承了unittest库里TestCase类的子类，运行所有以 test_ 开头的方法，然后展示测试结果












