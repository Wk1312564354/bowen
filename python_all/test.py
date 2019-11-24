#!/usr/bin/python
# -*-coding:utf8-*-

# 判断三角形
# a = int(input("输入三角形的边"))
# b = int(input("输入三角形的边"))
# c = int(input("输入三角形的边"))
# if ((a + b > c) and (a - b < c)):
#     if(a ** 2 + b ** 2 > c**2):
#         print("锐角三角形")
#     elif(a ** 2 + b ** 2 == c**2):
#         print("直角三角形")
#     else:
#         print("钝角三角形")
# else:
#     print("您输入的边长无法组成三角形")


# 判断是否回文
# a = input("输入一串字符串:")
# if len(a) % 2 == 0:
#     for i in range(1, len(a)+1):
#         if a[i-1] == a[-i]:
#             if i == len(a):
#                 print("%s是回文" % a)
#         else:
#             print("%s不是回文" % a)
#             break
# else:
#     print("%s不是回文" % a)


#  显示第一大和第二大的数字
# a = [1,2,3,3,3,4,4]
# b = []
# for i in range(len(a)):
#     m = max(a)
#     b.append(m)
#     a.remove(m)
# print(b)

# 所以的元素向左移动一位
# a = [1, 2, 3, 4, 5, 6]
# a.append(a[0])
# a.remove(a[0])
# print(a)

# 100块买100只鸡
# for i in range(101):
#     for j in range(101):
#         for k in range(101):
#             if i + j + k ==100:
#                 if 2 * i + j + 0.5 * k ==100:
#                     print(i, j, k)

#  十进制转十六进制
# a = int(input("输入一个十进制数："))
# i = 1
# b = []
# while i > 0:
#     if a % 2 == 0:
#         a = a // 2
#         b.append("0")
#     else:
#         a = a // 2
#         b.append("1")
#     if a == 0:
#         break


# txt = open(r"a.txt", "r", encoding="utf8")
# while 1:
#     a = txt.readline()
#     if "abc" in a:
#         print(a)
#     elif a == "":
#         break
# txt.close()



# def wk(x):
#     a = []
#     b = []
#     a.extend(x)
#     a = list(set(a))
#     b.append(max(a))
#     a.remove(max(a))
#     b.append(max(a))
#     for i in x:
#         if i in b:
#             print(i)
#
# a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
# wk(a)

import wk.day1
def zzz():
    print(666)
    wk.day1.ha()
    wk.day1.wo()

zzz()


