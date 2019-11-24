#!/usr/bin/python
# -*-coding:utf8-*-
# while 1:
#     i = input("请输入一个字符串：")
#     if i == "exit":
#         break
#     a = i.replace(" ", "").title().replace("a", "123")
#     print(a)

# a = [12, 123, 1234, 12, 32, 12]
# b = []
# for i in a:
#     if i in a:
#         if i not in b:
#             b.append(i)
# print(b)

# a = [12, 123, 1234, 32, 12, 12, 12, 64, 12, 123]
# for i in a:
#     b = a.count(i)
#     if b > 1:
#         for j in range(a.count(i)-1):
#             a.remove(i)
# print(a)


# for i in range(0, 101):
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
#         print(i, end=" ")

# i = 2
# a = 0
# while i < 100:
#     b = 1
#     while b <= i:
#         if i % b == 0 and i != b and b != 1:
#             break
#         b += 1
#     else:
#         a += i
#     i += 1
# print(a)

# 三次猜数字
# import random
# a = random.randint(0, 10)
# # print(a)
# for i in range(3):
#     b = int(input("请输入你猜的数字："))
#     if b > a:
#         if i == 2:
#             continue
#         print("大了,还剩下%d次机会哦" % (2-i))
#     elif a < b:
#         if i == 2:
#             continue
#         print("小了,还剩下%d次" % (2-i))
#     else:
#         print("你真棒！")
#         break
# else:
#     print("这都猜不对？")

# 打印 user1 到 user50
# i = 1
# while i <= 50:
#     print("user %d" % i)
#     i += 1

# a = input("请输入一串数据(注意用空格隔开)：")
# b = a.split(" ")
# c = []
# d = []
# for i in b:
#     c.append(int(i))
# for j in range(0,len(c)):
#     m = min(c)
#     d.append(m)
#     c.remove(m)
# print(d)
# 冒泡法
# for i in range(len(c)-1):
#     for j in range(len(c)-1):
#         if c[j] > c[j + 1]:
#             c[j], c[j + 1] = c[j + 1], c[j]
# print(c)

# a = (2, 12, 55, 36, 45, 89)
# print(len(a))
# a = {
#     "name": "wk",
#     "age": [19, 20, 21],
#     "sex": "男"
#     }
# a.popitem()
# a.pop("sex")
# a.keys()
# print(a.items())

# a = [11, 22, 33, 44, 55, 66, 77, 88]
# i = []
# j = []
# b = {"k1": [],"k2": []}
# for k in a:
#     if k > 55:
#         i.append(k)
#     elif k < 55:
#         j.append(k)
# b["k1"] = i
# b["k2"] = j
# print(b)

# dic = {"k1": "alex", "k2": " aric", "k3": "Alex", "k4": "Tony"}
# a = dic.values()
# b = list(a)
# for i in b:
#     i = i.replace(" ", "")
#     if (i.startswith("a") or i.startswith("A")) and i.endswith("c"):
#         print(i)

# li = [1, 2, 3, "a", 4, "c"]
# dic = {}
# dic["k1"] = []
# for i in li:
#     if li.index(i) % 2 == 1:
#         dic["k1"].append(i)
# print(dic)


# a= ["wk", "wkk", "wwkk"]
# for i, j in enumerate(a):
#     print(i, j)

# a = {55, 123, 100, 1000, 52}
# a.add("sss")
# print(a)


# li = ["手机", "电脑", "鼠标垫", "游艇"]
# for i, j in enumerate(li):
#     print(i, j)
# a = int(input("请输入你要了解的商品号码"))
# print(li[a])
