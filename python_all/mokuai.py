#!/usr/bin/python
# -*-coding:utf8-*-

# 导入模块

# def wk():
#     print("666")
#
# def wkk():
#     print("dnf")
#
#
# if __name__ == "__main__":
#     print("666")



# try:
#     a = "123456"
#     int(a)
# except Exception as f:
#     print(f)
# # except ValueError:
# #     print("6")
# else:
#     print("123")
# finally:
#     print("8888")

# raise SyntaxError("这是一个语法错误")


# 类名
# 类分两种： 1，经典类 Class Dog:     2，新式类  Class Dog(object)

# class Dog:

# 类的行为
#     def run(self):
#         print("---跑---")
#     def pee(self):
#         print("---撒尿---")
#     def info(self):
#         self.run()
#         self.pee()
#         print(self.color)
#         print(self.name)
#         print(self.sex)
#         print(self.legCount)

# 类的实例
# Husky = Dog()
# Husky.name = "qiqi"
# Husky.color ="黑白"
# Husky.sex = "公"
# Husky.legCount = "4"
# # Husky.run()
# # Husky.pee()
# Husky.info()
# Samoyed = Dog()
# Samoyed.run()
# Samoyed.pee()

# class Dog:
#     def __init__(self, color, leg):
#         self.color = color
#         self.leg = leg
#         print(self.color)
#         print(self.leg)
#     def pee(self):
#         print("---撒尿---")
#
#
# BigDog = Dog("黄色", "4条腿")
# BigDog.pee()


# class Waou():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __hanshu(self, name, sex="男", *args, **kwargs):
#         print(name, sex, args, kwargs)
#         print(self.name)
#         print(self.age)
#
#
# a = Waou("wkk", 21)
# # a.hanshu("wk", "男", 12, 11, 14, 15, 16, 13, 42, lalal="666")
# print(a.age)




