#!/usr/bin/python
# -*-coding:utf8-*-

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




