#!/usr/bin/python
# -*-coding:utf8-*-
# 利用print , input,占位符，买苹果
price = float(input("请输入单价:"))
weight = float(input("请输入重量:"))
Total_price = price * weight
Total_price -= 5
print("苹果的单价是： %.2f ,苹果的重量是： %.2f ,总价钱是： %.2f"  %(price,weight,Total_price))

# if语句 上网
age = int(input("请输入你的年龄"))
if age >= 18:
    print("去网吧happy!!!")
else:
    print("滚一边去")

# bool类型
is_employee = bool(input("是否是本公司员工"))
if not is_employee:
    print("不允许入内")
else:
    print("请进")

# 多分枝if语句  if...elif...else...
holiday_name = str(input("节日名称:"))
if holiday_name == "情人节":
    print("买玫瑰 看电影")
elif holiday_name == "生日":
    print("买蛋糕")
elif holiday_name == "平安夜":
    print("买苹果")
else:
    print("每天都是你的节日")

# 坐火车过安检
ticket = int(input("是否有车票"))
if ticket == 1:
    print("第一次安检通过")
    knife_length = int(input("刀的长度"))
    if knife_length >=20:
        print("刀的长度为 %d cm 没收刀具" %knife_length)
    else:
        print("可以上车")
else:
    print("无法通过")

# 判断成绩
score = int(input("请输入你的成绩："))
if 0 <= score <= 100:
  while score in range(0,100):
    if 90 <= score <= 100:
        print("优秀")
        break
    elif 70 <= score < 90:
        print("一般")
        break
    elif 60 <= score < 70:
        print("及格")
        break
    else:
        print("不及格")
        break
else:
  print("请重新输入分数")

#输入一个数，判断能否被2或3整除
number = int(input("请输入一个数字"))
if number % 2 == 0 or number % 3 == 0:
    print("")
    if number % 2 != 0:
        print("hello")
    elif number % 3 != 0:
            print("world")
    else:
        print("helloworld")
else:
    print("123")

# 和电脑对战猜拳
import random
while 1:
    # 石头 1   剪刀 2   布 3
    player = int(input("来吧，出拳一战!"))
    computer = random.randint(1,3)
    if (player == 1 and computer ==2) or (player == 2 and computer == 3) or (player ==3 and computer ==1):
        print("玩家赢")
    elif(player == computer):
        print("平局")
    else:
        print("电脑赢")


# 水仙花数
for i in range(1001):
    b = i // 100
    s = i % 100 //10
    g = i % 100 % 10
    if b ** 3 + s ** 3 + g ** 3 == i:
        print(i)


# 冒泡法排序
a = [15,11,37,20,10,1,21,5]
for k in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i + 1]:
            a[i],a[i + 1]=a[i + 1],a[i]
print(a)

# 选择法排排序
a = [25,20,11,14]
for j in range(len(a)-1):
    for i in range(len(a)-1):
        for k in range(i，len(a)-1):
            if a[i] > a[k + 1]:
                a[i],a[k + 1]=a[k + 1],a[i]
print(a)


# 利用max,min排序
a = [20, 25, 17, 37, 5]
b = []
for i in range(len(a)-1):
    m = min(a)
    b.append(m)
    a.remove(m)
a = b
print(a)


#九九乘法表
i = 1
while i<= 9:
    k = 1
    while k <= i:
        print("{} * {} = {}".format(k , i ,i * k),end="\t")
        k += 1
    print("")
    i += 1


# 质数之和
m = 0
for i in range(1,101):
    for j in range(1,i):
        if i % j == 0:
            continue
        else:
            m += i
print(m)


# 字符串以A和a开头，以c结尾
a = ["ABC", "abc", "abb", "cda"]
for i in a:
    if (i.startswith("a") or i.startswith("A")) and i.endswith("c"):
        print(i)


# 逢7过
for i in range(0, 101):
    if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        print(i, end=" ")


# 不用int将字符串化成整数
a = "12345678"
a = a[::-1]
c = 0
print(a)
for i in a:
    for j in range(10):
        if i == str(j):
            b = j * 10 ** a.index(i)
    c += b
print(type(c))
print(c)


# 判断三角形
a = int(input("输入三角形的边"))
b = int(input("输入三角形的边"))
c = int(input("输入三角形的边"))
if ((a + b > c) and (a - b < c)):
    if(a ** 2 + b ** 2 > c**2):
        print("锐角三角形")
    elif(a ** 2 + b ** 2 == c**2):
        print("直角三角形")
    else:
        print("钝角三角形")
else:
    print("您输入的边长无法组成三角形")


# 100块买100只鸡
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i + j + k ==100:
                if 2 * i + j + 0.5 * k ==100:
                    print(i, j, k)


# 所以的元素向左移动一位
a = [1, 2, 3, 4, 5, 6]
a.append(a[0])
a.remove(a[0])
print(a)


# 判断是否回文
a = input("输入一串字符串:")
if len(a) % 2 == 0:
    for i in range(1, len(a)+1):
        if a[i-1] == a[-i]:
            if i == len(a):
                print("%s是回文" % a)
        else:
            print("%s不是回文" % a)
            break
else:
    print("%s不是回文" % a)


#将十进制转换为二进制
a = int(input("请输入一个数字："))
i = []
while a > 0:
    if a % 2 == 0:
        a = a / 2
        i.append("0")
    else:
        a = (a - 1) /2
        i.append("1")
i = "".join(i)
i = i[::-1]
print(i)


# 十进制转十六进制
a = int(input("输入一个十进制数："))
i = 1
b = []
while i > 0:
    if a % 2 == 0:
        a = a // 2
        b.append("0")
    else:
        a = a // 2
        b.append("1")
    if a == 0:
        break


# txt文件内写内容 九九乘法表
txt=open('a.txt','w',encoding='utf8')
for i in range(1,10):
    for a in range(1,i+1):
        txt.write(f'{a}*{i}={a*i}\t')
    txt.write('\n')
txt.close()


# txt文件中读  去除空行和以“#”开头的
txt=open(r'D:\python\123.py','r',encoding='utf8')
a = txt.read()
print(a)
txt.close()

txt=open('a.txt','r',encoding='utf8')
while True:
    c = txt.readline()
    print(c)
    if c == '\n':
        break
txt.close()

txt=open('a.txt','r',encoding='utf8')
c = txt.readlines()
print(c)
txt.close()

a=open('for循环.py','r',encoding='utf8')
c = a.readlines()
print(c)
a.close()

a=open('for循环.py','r',encoding='utf8')
i = 0
j = 0
while 1:
    c = a.readline()
    if c.startswith('#'):
        i += 1
    elif c == '\n':
        j += 1
    elif c == '':
        break
print(i,j)
a.close()


# txt文件中追加
txt=open('a.txt','a',encoding='utf-8')
txt.write('\nxkljaslkc')
txt.close()



# 购物车
goods = [
    {"name": "电脑", "price": 19999},
    {"name": "键盘", "price": 200},
    {"name": "鼠标", "price": 100},
    {"name": "主机", "price": 3000}
        ]
D_price = 0                     # 单个商品的总价格  用户购买单个商品名 * 数量
total_price = 0                 # 购物车内所有商品的总价格
z = 1
p = 1
                                # 三个组分别存储了购物车内所有的商品，数量，价格
m = []
h = []
f = []
money = int(input("请输入你的资产："))
while z:
    print("欢迎光临！")
    w = 1
    z = 0
    v = 1
    while w:
        z = 1
        print("编号 商品 价格")
        for i, j in enumerate(goods):                               # 依次取出商品的编号，商品名，单价
            print(i, goods[i]["name"], goods[i]["price"])
        print("您可以添加您喜欢的商品到购物车中")
                            # 购物模块
        while 1:
            Id = int(input("请输入你要加入购物车的商品的编号："))     # 依据用户输入的商品名和数量算出价格和购物车内的总价格
            No = int(input("请输入您要购买的数量:"))
            D_price += goods[Id]["price"] * No
            f.append(D_price)
            total_price += D_price
            n = goods[Id]["name"]
            m.append(n)
            h.append(No)
            print("您购物车里的宝贝有{} 数量{} 价格{}".format(m, h, f))
            print("您所选购的商品的总价格是： %0.2f" % total_price)
            Ts = input("你还要继续选择商品吗？(是  or   否)")        # 判断是否继续选择商品，否 的话跳出购物阶段的while循环
            if Ts == "是":
                print("请您继续选择商品")
            else:
                break
                                    # 付款准备模块
        pay = input("您是否现在付款？")
        if pay == "是":
            print("请确认您的支付订单并付款")
            print("您本次消费共计%0.2f" % total_price)
            print("您购物车里的宝贝有{} 数量{} 价格{}".format(m, h, f))
            print("您所选购的商品的总价格是： %0.2f" % total_price)
            car = input("您可以选择性的移除您购物车中的宝贝，您要执行操作么？(是   or  否)")
            if car == "是":                  # 可根据购物车的物品选择是否删除
                while 1:
                    Cid = int(input("请输入你像删除的我物品在购物车中的位置"))
                    Cno = int(input("请输入您要删除物品的数量"))
                    total_price -= f[Cid] // h[Cid] * Cno          # 删除物品是数据的改动
                    f[Cid] -= f[Cid] // h[Cid] * Cno
                    h[Cid] = h[Cid] - Cno
                    if h[Cid] == 0:
                        h.pop(Cid)
                        m.pop(Cid)
                        f.pop(Cid)
                        print("你的购物车空空的。。。")
                        break
                    print(total_price)
                    print("您购物车里的宝贝有{} 数量{} 价格{}".format(m, h, f))
                    TT = input("是否还有继续删除物品？(是  or   否)")
                    if TT == "否":
                        break
                            # 付款模块
            Check = input("您是否要付款？(是   or  否)")
            if Check == "是":
                while v:
                    print("正在处理，请稍后。。。")
                    if money >= total_price:
                        money = money - total_price
                        print("您的余额还剩%0.2f元" % money)
                        print("谢谢惠顾")
                        m.clear()
                        h.clear()
                       # total_price = 0
                        z = 0
                        v = 0
                        break
                                # 余额不足是选择删除商品或充值
                    else:
                        choose = input("您的余额不足，还缺少{}你是选择删除商品还是充值呢？(删除  or  充值)".format(total_price-money))
                        if choose == "删除":                             # 移除商品
                            while p:
                                Cid = int(input("请输入你像删除的我物品在购物车中的位置"))
                                Cno = int(input("请输入您要删除物品的数量"))
                                total_price -= f[Cid] // h[Cid] * Cno
                                f[Cid] -= f[Cid] // h[Cid] * Cno
                                h[Cid] = h[Cid] - Cno
                                if h[Cid] == 0:
                                    h.pop(Cid)
                                    m.pop(Cid)
                                    f.pop(Cid)
                                    print("你的购物车空空的。。。")
                                    break
                                print("您购物车里的宝贝有{} 数量{} 价格{}".format(m, h, f))
                                Go_on = input("请你选择是继续删除物品还是付款？(删除    or   付款)")
                                if Go_on == "付款":
                                    break
                        else:
                            print("您的余额不足，请您充值")            # 充值
                            ts = input("您是否充值？(是  or  否)")
                            if ts == "是":
                                C_money = int(input("请输入充值金额："))
                                money = money + C_money
                                print("正在为您完成订单支付")
                            else:
                                v = 0
                                break
    print("谢谢惠顾")
    w = 0
# 人狗大战

class People():
    def __init__(self, name, HP=100, ATK=5):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.Big_move = "打狗棍法"
        self.dogHP = 1

    def __str__(self):
        UI = "玩家：" + self.name + "\n" + "血量：" + str(self.HP) + "\n" + "攻击力：" + str(self.ATK) + "\n"
        UI += "终极技能：" + self.Big_move + "\n"
        if self.dogHP <= 0:
            UI += "狗死了，人类胜利！"
        elif self.dogHP == 50:
            UI += "发动打狗棍法"
            self.ATK += 10
        return UI

    def attack(self, dog):
        if dog.HP > 0:
            dog.HP -= self.ATK
        self.dogHP = dog.HP


class Dog():
    def __init__(self, name, HP=100, ATK=2):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.Big_move = "狂犬病毒"
        self.peopleHP = 1

    def __str__(self):
        UI = "恶犬：" + self.name + "\n" + "血量：" + str(self.HP) + "\n" + "攻击力：" + str(self.ATK) + "\n"
        UI += "终极技能：" + self.Big_move + "\n"
        if self.peopleHP <= 0:
            UI += "很不幸，恶犬咬死了您。。。"
        elif 3 <= (100 - self.HP) // 10 <= 4:
            UI += "恶犬在下次攻击会发动 狂犬病毒 "
        return UI

    def attackd(self, people):
        if people.HP > 0:
            people.HP -= self.ATK
            if 3 <= (100 - self.HP) // 10 <= 4:
                people.HP -= 20
        self.peopleHP = people.HP


p1 = People("God")
print(p1)
p2 = People("Alen", 80, 10)
print(p2)
g1 = Dog("地狱三头犬")
print(g1)
while 1:
    p1.attack(g1)
    p2.attack(g1)
    g1.attackd(p1)
    g1.attackd(p2)
    if g1.HP <= 0:
        g1.HP = 0
        print(g1)
        print(p1)
        print(p2)
        break
    elif p1.HP == 0 or p2.HP == 0:
        break
    print(g1)
    print(p1)
    print(p2)


# Excel中写九九乘法表
import xlwt
a = xlwt.Workbook(encoding="utf8")    # 写入excel格式
sheet = a.add_sheet("wkk")            # 添加一个标签页
sheet1 = a.add_sheet("666")
for i in range(1, 10):
    for j in range(1, i+1):
        print("{} * {} = {}".format(j, i, j*i), end="\t")
        sheet.write(i-1, j-1, "{} * {} = {}".format(j, i, j*i))
a.save("wk.xls")


#将Excel表格中的九九乘法表写入txt文件中
import xlwt

file = xlwt.Workbook(encoding="utf8")
sheet = file.add_sheet("凉城")
for i in range(1, 10):
    for j in range(1, i+1):
        sheet.write(i-1, j-1, "{} * {} = {}".format(j, i, i*j))
file.save("wk.xls")

import xlrd
txt = open("c.txt", "w", encoding="utf8")
file1 = xlrd.open_workbook("wk.xls")
sheet1 = file1.sheet_names()
print(sheet1)
sheet2 = file1.sheet_by_name("凉城")
for i in range(sheet2.nrows):
    # for j in range(len(sheet2.row_values(i))):
    for j in range(i+1):
        content = sheet2.cell(i, j).value
        txt.write("{}\t".format(content))
    txt.write("\n")
txt.close()


# 爬虫，爬小说
import requests
import re
from time import *
with open(r"c:\Users\wk\Desktop\wenjian.txt", "a", encoding="utf8") as txt:
    k = 0
    for i in range(264, 702):
        a = requests.get("http://www.quanshuwang.com/book/9/9055/9674{}.html".format(i))
        content1 = a.content.decode("gbk")
        title = re.findall(re.compile('<strong class="l jieqi_title">(.*?)</strong><a href="', re.S), content1)
        file = re.findall(re.compile('<div class="mainContenr"(.*?)<script type="text/javascript">style6', re.S), content1)
        file = file[0] + "<br />"
        file1 = re.findall(re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />', re.S), file)
        txt.write("\t\t\t\t\t\t\t"+title[0]+"\n\n")
        for j in file1:
            txt.write(j + "\n")
        sleep(5)
        k += 1
        print("》"*(k//4),"已完成{}%".format((k//4)))


# 爬虫，爬图片
import requests
import re
image = requests.get("http://www.mmonly.cc/sgtp/")
reponse = image.content.decode("gbk")
regular = re.compile('<div class="img">(.*?)original',re.S)
filtrate = re.findall(regular, reponse)
# print(filtrate)
a = re.findall(re.compile('alt="(.*?)" src',re.S), str(filtrate))
b = re.findall(re.compile('src="(.*?)" ',re.S), str(filtrate))
yaSuo = zip(a, b)
for i,j in yaSuo:
    response = requests.get(j)
    picture = response.content
    with open(r"c:\Users\wk\Desktop\tupian\{}.jpg".format(i),"wb") as f:
        f.write(picture)


# 爬虫，爬视频
import requests
import re
html = requests.get("https://www.pearvideo.com/category_8")
response = html.content.decode("utf8")
result = re.compile('<div class="vervideo-bd">(.*?)class="vervideo-lilink actplay">',re.S)
filrate = re.findall(result, response)
# print(filrate)
file = re.findall(re.compile('<a href="(.*?)"',re.S), str(filrate))
# print(file)
for i in file:
    html1 = requests.get("https://www.pearvideo.com/{}".format(i))
    response1 = html1.content.decode("utf8")
    file1 = re.findall(re.compile(',srcUrl="(.*?)",',re.S), response1)
    # print(file1)
    video = requests.get(file1[0])
    video_response = video.content
    with open(r"c:\Users\wk\Desktop\新建文件夹\{}.mp4".format(i), "ab") as f:
        f.write(video_response)


# 爬虫，爬智联招聘
def zhilian():
    import requests
    import json

    url = "https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.01804714&x-zp-page-request-id=4d3bb4ec70a84d8c9ebdcd3774dda842-1572655938282-616161&x-zp-client-id=f8bf232b-a88f-46c9-bd1e-7bd8abbf5c97"
    head = {'Host':'fe-api.zhaopin.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept':'application/json, text/plain, */*',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate, br',
    'Origin':'https://sou.zhaopin.com',
    'Connection':'keep-alive',
    'Referer':'https://sou.zhaopin.com/?jl=530&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3',
    'Cookie':'urlfrom2=121113803; adfcid2=pz_bg_beijingzhiwei; adfbid2=0; x-zp-client-id=f8bf232b-a88f-46c9-bd1e-7bd8abbf5c97; sts_deviceid=16d39617941181-008b12d10474e28-4c312373-1327104-16d3961794244b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d3961795a449-04f781cef2d361-4c312373-1327104-16d3961795b131%22%2C%22%24device_id%22%3A%2216d3961795a449-04f781cef2d361-4c312373-1327104-16d3961795b131%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0jZ7-0KqiAs0bYekI00000rbOfNC00000T1BdaZ.THLyktAJ0A3qUyq8UA-8uNt1gvwM0ZnqmHT1rjP-nWbsnjKWm19-r0Kd5HFDnbD3fYckfbuDrHP7nbmzP1RYn10kP10%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%2C%22%24latest_utm_campaign%22%3A%22hydt%22%2C%22%24latest_utm_content%22%3A%22tj%22%2C%22%24latest_utm_term%22%3A%2228720337%22%7D%7D; dywea=95841923.4317923423887511600.1569311447.1569311447.1572591894.2; dywez=95841923.1572591894.2.2.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1572591895,1572655929; __utma=269921210.36310528.1569311449.1569311449.1572591895.2; __utmz=269921210.1572591895.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; sou_experiment=unexperiment; acw_tc=3ccdc15715725918944414277e3fe0467d47d8ae37b88787c3de98fd76406a; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; ZP_OLD_FLAG=false; POSSPORTLOGIN=1; CANCELALL=1; urlfrom=121113803; adfcid=pz_bg_beijingzhiwei; adfbid=0; ZL_REPORT_GLOBAL={%22//www%22:{%22seid%22:%22%22%2C%22actionid%22:%2275307dee-4251-4019-b258-0fd6dab90314-cityPage%22}%2C%22sou%22:{%22actionid%22:%2221209f38-24d7-44aa-b3f1-88e8fe984a7e-sou%22%2C%22funczone%22:%22smart_matching%22}}; sts_sg=1; sts_evtseq=8; sts_sid=16e2998ed5314d-00fdbf12cee19f8-4c302b7a-1327104-16e2998ed54111; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0jZ7-0KqiAs0bYekI00000rbOfNC00000T1BdaZ.THLyktAJ0A3qUyq8UA-8uNt1gvwM0ZnqmHT1rjP-nWbsnjKWm19-r0Kd5HFDnbD3fYckfbuDrHP7nbmzP1RYn10kP103nHc1nbfz0ADqI1YhUyPGujY1nW63rHb3nWbdFMKzUvwGujYkP6K-5y9YIZK1rBtEmv4YQMGCmyqspy38mvqVQYd9ThV-IaqLpAq_uNqWULN8IANzQhG1Tjq1pyfqnHcknHD1rj01FMPGIARqTZGxmhIxmhNGph-8uLGCpgI-piudThsqpZwYTZnlQzqLILT8Xh99ULKGUB4WUvYEmhNGph-8uztOIgwVgLPEIgFWuHdBmy-bIgKWTZChIgwVgvd-uA-dUHdWTZf0mLFW5HR1PWnL%26tpl%3Dtpl_11534_19968_16032%26l%3D1514225641%26attach%3Dlocation%253D%2526linkName%253D%2525E8%2525A1%2525A8%2525E6%2525A0%2525BC%2525E7%2525BB%252584%2525E4%2525BB%2525B6-%2525E8%2525A1%2525A8%2525E6%2525A0%2525BC%2525203-1%2526linkText%253D%2525E5%25258C%252597%2525E4%2525BA%2525AC%2525E8%252581%25258C%2525E4%2525BD%25258D%2526xp%253Did(%252522m3288998295_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B3%25255D%25252FDIV%25255B1%25255D%25252FTABLE%25255B1%25255D%25252FTBODY%25255B1%25255D%25252FTR%25255B3%25255D%25252FTD%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D11%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_3_dg%26wd%3D%25E6%2599%25BA%25E8%2581%2594%26oq%3D%25E6%2599%25BA%25E8%2581%2594%26rqlang%3Dcn; jobRiskWarning=true; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1572655929',
    'TE': 'Trailers'}
    html = requests.get(url,headers=head)
    content = html.json()
    return content

def create_Excel():
    import xlwt
    excel_Format = xlwt.Workbook(encoding="utf8")
    sheet = excel_Format.add_sheet("智联-北京")
    excel_Format.save("智联.xls")


def reading_Data(Data,i):
    city = Data["data"]["results"][i]["city"]["display"]
    company = Data["data"]["results"][i]["company"]["name"]
    jobname = Data["data"]["results"][i]["jobName"]
    salary = Data["data"]["results"][i]["salary"]
    return city,company,jobname,salary

def addTo_Excel(nums,html):
    import xlrd
    from xlutils.copy import copy
    excel_Data = xlrd.open_workbook("智联.xls")
    new_Data = copy(excel_Data)
    sheet1 = new_Data.get_sheet("sheet1")
    for i in range(nums):
        for j in range(4):
            sheet1.write(i, j, reading_Data(html,i)[j])
    new_Data.save("智联.xls")

from time import *
html = zhilian()
sleep(1)
# create_Excel()
sleep(1)
addTo_Excel(50,html)


#

