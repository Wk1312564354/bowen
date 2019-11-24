#!/usr/bin/python
# -*-coding:utf8-*-

txt = open(r"c:\Users\wk\Desktop\u=3982432042,3723054889&fm=26&gp=0.gif", "rb")
# txt.write("nihao\n")
# txt.write("不开心\n")
# # txt.close()
# # def jiujiu():
# i = 1
# while i <= 9:
#     k = 1
#     while k <= i:
#         txt.write(f" {i} * {k} = {i*k} ")
#         k += 1
#     txt.write("\n")
#     i += 1
# txt.close()
# for i in range(25):
#     txt.write("王" * 4)
#     txt.write("\n")
#
# for i in range(2):
#     txt.write("王" * 50)
#     txt.write("\n")
# # txt.write("\n")
# for j in range(20):
#     txt.write("王" * 2)
#     txt.write("昆" * 46)
#     txt.write("王" * 2)
#     txt.write("\n")
# # txt.write("\n")
# for k in range(2):
#     txt.write("王" * 50)
#     txt.write("\n")
# txt.close()
#
# while 1:
#     a = txt.readline()
#     if a == " ":
#         break
#     print(a)
#     print(type(a))
#
# def wk(w="666"):
#     print(w)
#
#
# wk()


# while 1:
#     a = txt.readline()
#     print(a)
#     if a == "":
#         break
# print(txt.readlines())
# print(len(txt.readlines()))
# txt.close()



# print(txt.readlines())
# m = 0
# n = 0
# k = len(txt.readlines())
# while 1:
#     a = txt.readline()
#     if a == "\n":
#         m += 1
#     elif a.startswith("#"):
#         n += 1
#     elif a == "":
#         break
#     else:
#         pass
# print(m, n)
# txt.close()

# a = txt.readline()
# b = txt.readlines()
# print(a)
# print(b)

# txt.write("asdfgh\n")
# txt.write("qwertyuiop")
# txt.write("zmlzml")
# print(txt.readlines())
# txt.write("zml")
# a = txt.read()
# txt.close()
# b = open(r"b.gif","wb")
# b.write(a)
# b.close()

with open("a.txt", "r", encoding="utf8") as f:
    print(f.read())
