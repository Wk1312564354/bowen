#!/usr/bin/python
# -*-coding:utf8-*-
# i = input("请输入一串纯字母的字符串：")
# a = list(set(i))
# print(a)
# b = 0
# c = []
# for j in a:
#      b = i.count(j)
#      c.append(str(b) + j)
# print(c)
# for k in range(len(c)):
#     m = max(c)
#     print(m[-1])
#     c.remove(m)


# def zhishu(x=1,y=100):
#     for i in range(x, y+1):
#         a = 0
#         for j in range(1, i):
#             if i % j == 0 and i != j:
#                 a += j
#         if i == a:
#             print(a)


# zhishu(y=1000)

# b = [i ** 2 for i in range(2, 11) if i % 2 == 0]
# print(b)

# def biao():
#     global a
#     a = [11, 22, 33, 44, 55, 66, 77, 88, 99]
#     b = [i for i in a if i > 55]
#     c = [j for j in a if j < 55]
#     print(b)
#     print(c)
#
# biao()
# print(a)


# def haha(x):
#     a = sum(range(x+1))
#     print(a)
#
#
# haha(100)
# a = [1,2]

# def wk(*x):
#     print(x)
#
# wk([123,111,21],147,"dfd")

# def sum1(x):
#     a = sum(range(x+1))
#     print(a)
#     return a
#
#
# def sum2(x):
#     a = [i for i in range(1,x,2)]
#     b = sum(a)
#     print(b)
#
#
# c = sum1(10)
# print(c)


# def wk(b, *a):
#     a = list(a)
#     for i in range(len(a)):
#         for j in range(i+1, len(a)):
#             if a[i] + a[j] == b:
#                 print(a[i], a[j])
#
#
# wk(10, 1, 2, 3, 4, 7, 8, 9, 10)

# a = [1, 2, 3, 4, 5, 6]
# print(a[-1::-2])

# a = "12345678"
# a = a[::-1]
# c = 0
# print(a)
# for i in a:
#     for j in range(10):
#         if i == str(j):
#             b = j * 10 ** a.index(i)
#     c += b
# print(type(c))
# print(c)

# def wk():
#     a = 1
#     def wkk():
#         print(123)
#     return wkk
#
#
# wk()()
# print(wk()())


# wk = lambda x, y:x * y if x!=y else 0
# print(wk(14,5))

# m = 0
# i = 1
# a = int(input("输入你刚开始有多少钱:"))
# b = int(input("没花费多少钱的可以得到1元:"))
# while i > 0:
#     if i % b == 0:
#         a = a + 1
#         a -= 1
#     else:
#         a -= 1
#     m += 1
#     if a == 0:
#         break
#     i += 1
# print(m)

# txt=open('b.txt', 'w' ,encoding='utf8')
# q = '白苗    '
# txt.write(' '*8)
# txt.write(f'{q}'*1)
# txt.write(' '*16)
# txt.write(f'{q}'*1)
# txt.write('\n')
# txt.write(' '*4)
# txt.write(f'{q}'*2)
# txt.write(' '*8)
# txt.write(f'{q}'*2)
# txt.write('\n')
# txt.write(f'{q}'*6)
# txt.write('\n')
# txt.write(f'{q}'*6)
# txt.write('\n')
# for a in range(6):
#     txt.write(' ' * (a*4))
#     txt.write(f'{q}' * (6-a))
#     txt.write('\n')
# txt.close()
