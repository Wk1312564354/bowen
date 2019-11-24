# print("美玲")       # 输出美玲
# # 输出美玲
# print("美玲")
# print(8//3)
"""
色色得瑟
得
瑟
"""
'''
名字是输出的结果
输入美玲'''
"""name =input("请输入名字：")
print(name)

a = 2
b = 3
c = a+b
print(c)
qq_number = "1312564354"
qq_password = "123456"
print(qq_password)


qq = input("输入QQ号码")
qm = input("输入密码")
print(qq)
print(qm)
print("登陆成功")
"""
price = float(input("请输入单价:"))
weight = float(input("请输入重量:"))
yingfu = price * weight
yingfu -= 5
print("苹果的单价是： %.2f ,苹果的重量是： %.2f ,总价钱是： %.2f"  %(price,weight,yingfu))
# a = 5
# b = 3
# c = a + b
# c -= 5
# print(c)
# name = "小玲"
# age = 18
# sex = True
# high = 1.65
# weight = 59
# name = "小明"
# print("我的名字叫 %s 请多关照！" % name)
# student_no = 1
# print("我的学号是： %06d" % student_no)
# scale = 10.00
# print("数据比例是 %.2f%%" %scale)
# age = int(input("请输入你的年龄"))
# if age >= 18:
#     print("去网吧happy!!!")
# else:
#     print("滚一边去")
# age = int(input("请输入你的年龄："))
# # if age > 0 and age <120:
# if 0 < age < 120:
#     print("yes")
# else:
#     print("no")
# python_score = int(input("输入python的成绩："))
# c_score = int(input("输入C的成绩："))
# if python_score >= 60 or c_score >= 60:
#     print("及格")
# else:
#     print("不及格")
# is_employee = bool(input("是否是本公司员工"))
# # #is_employee = True
# # if not is_employee:
# #     print("不允许入内")
# # else:
# #     print("请进")
# holiday_name = str(input("节日名称:"))
# if holiday_name == "情人节":
#     print("买玫瑰 看电影")
# elif holiday_name == "生日":
#     print("买蛋糕")
# elif holiday_name == "平安夜":
#     print("买苹果")
# else:
#     print("每天都是你的节日")
# ticket = int(input("是否有车票"))
# if ticket == 1:
#     print("第一次安检通过")
#     knife_length = int(input("刀的长度"))
#     if knife_length >=20:
#         print("刀的长度为 %d cm 没收刀具" %knife_length)
#     else:
#         print("可以上车")
# else:
#     print("无法通过")
# score = int(input("请输入你的成绩："))
# if 0 <= score <= 100:
#   while score in range(0,100):
#     if 90 <= score <= 100:
#         print("优秀")
#         break
#     elif 70 <= score < 90:
#         print("一般")
#         break
#     elif 60 <= score < 70:
#         print("及格")
#         break
#     else:
#         print("不及格")
#         break
# else:
#   print("请重新输入分数")
# number = int(input("请输入一个数字"))
# if number % 2 == 0 or number % 3 == 0:
#     print("")
#     if number % 2 != 0:
#         print("hello")
#     elif number % 3 != 0:
#             print("world")
#     else:
#         print("helloworld")
# else:
#     print("123")
# while 1:
#     # 石头 1   剪刀 2   布 3
#     player = int(input("来吧，出拳一战!"))
#     import random
#     computer = random.randint(1,3)
#     if (player == 1 and computer ==2) or (player == 2 and computer == 3) or (player ==3 and computer ==1):
#         print("玩家赢")
#     elif(player == computer):
#         print("平局")
#     else:
#         print("电脑赢")
# i = 0
# a = 0
# while i <= 100:
#     if i %2 == 0:
#         a += 0
#     else:
#         a += i
#     i += 1
#
# print(a)

# a = 1
# while a <=5:
#     b = 1
#     while b <= a:
#         print("*",end="")
#         b += 1
#     print("")
#     a += 1
# print("1\t2\t3")
# print("10\t20\t30")

# print("我叫\"张三\"")


# 九九乘法表
# i = 1
# while i <= 9:
#     k = 1
#     while k <= i:
#         print("%d * %d = %d" %(k,i,i*k), end="\t")
#         k += 1
#     print("")
#     i += 1


# 100内的质数之和

# i = 2
# k = 0
# while i <= 100:
#     if i %2 !=0 and i %3 != 0 and i %5 != 0 and i %7 != 0:
#         k += i
#     i += 1
# k = k + 2 + 3 + 5 + 7
# print(k)

# i = 2
# sum = 0
# while i <= 100:
#     k = 1
#     while k <= i:
#         if i % k ==0 and k != 1 and i != k:
#             break
#         k += 1
#     else:
#         sum += i
#     i += 1
# print(sum)


#
# import random
# while 1:
#     i = random.randint(1,4)
#     k = random.randint(1,4)
#     j = random.randint(1,4)
#     if i != k != j:
#         m = i * 100 + k * 10 + j
#         if k * 100 + j * 10 + i == m:
#             break
#         else:
#             print(m)


# i = 1
# while i <= 4:
#     h = i * 100
#     k = 1
#     while k <= 4:
#         m = k * 10
#         j = 1
#         while j <= 4:
#             if i != k and k  != j and i != j :
#                 print(h + m + j)
#             j += 1
#         k += 1
#     i += 1


# i = 100
# while i <= 999:
#     b = i // 100
#     s = i % 100 // 10
#     g = i % 100 % 10
#     if b ** 3 + s ** 3 + g ** 3 == i:
#         print(i)
#     i += 1

# for i in range(100,1000):
#     b = i // 100
#     s = i % 100 //10
#     g = i % 100 % 10
#     if b ** 3 + s ** 3 + g ** 3 == i:
#         print(i)

# a = [15 ,26 ,11 ,37,5]
# b = []
# m = 0
# # while len(a)!=len(b):
# for j in range(len(a)-1):
#     for i in range(len(a)-1):
#         m = a[i]
#         if a[j] > a[i + 1]:
#             a[j],a[i + 1]=a[i + 1],a[j]
#     b.append(m)
# print(b)

# a = [15,11,37,20,10,1,21,5]
# for k in range(len(a)-1):
#     for i in range(len(a)-1):
#         if a[i] > a[i + 1]:
#             a[i],a[i + 1]=a[i + 1],a[i]
# print(a)



# a = [25,20,11,14]
# for j in range(len(a)-1):
#     for i in range(len(a)-1):
#         for k in range(i，len(a)-1):
#             if a[i] > a[k + 1]:
#                 a[i],a[k + 1]=a[k + 1],a[i]
# print(a)

# a = 1
# b = 0
# c = 0
# while a <= 99:
#     if a % 2 == 1:
#         b += a
#     else:
#         c += a
#     a += 1
# print(b-c)











