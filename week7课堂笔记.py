# Author: keyin
# Date: week07 列表练习 & 初始字典

# 1.课本练习1

# 目标： “Don't panic” ==> "on tap"

# 方法一： 使用list的方法完成
phrase = "Don't panic!"
plist = list(phrase)  # list() 可以将 str  to(转)  list
print(phrase)
print(plist)

# 1.删除后面四个元素 a n i c
for i in range(4):
    plist.pop()
print(plist)
# 2. 删除 D  ‘
plist.remove('D')
print(plist)
plist.pop(2)
print(plist)

# 3. 数学案例： 计算 （(a+b)*(c+d)）
plist.extend([plist.pop(),plist.pop()])
#['o','n','t',' '][ a    ,   p     ]
print(plist)

# 4. 数据插入  实现：’t‘ 和’ ‘ 的位置转换
# plist.insert(2,plist.pop(3))
# print(plist)
# print(plist.pop(2))  # 1，代表删除的内容的值 2，他删除了plist的这个值
plist.insert(3,plist.pop(2))
print(plist)
# 5. list to str
new_phrase = ''.join(plist)


print(plist)
print(new_phrase)

# plist 改变了原先的状态么？ 列表的方法会改变列表本身，如果不想打破或者想保留原先数据的内容，请先用copy()复制数据


# 2.课本练习1-切片

# 方法二： 使用切片的方法实现

phrase = "Don't panic!"
plist = list(phrase)  # list() 可以将 str  to(转)  list
print(phrase)
print(plist)


on_str = ''.join(plist[1:3])
print(on_str)
new_phrase = on_str+ ''.join(plist[5]+plist[4]+plist[7]+plist[6])
print(plist)
print(new_phrase)


# 3.知识点-元组
t = 12345, 54321, 'hello!'
print(t)
print(type(t))
t.

# import time
# print(time.localtime())


# 4.课堂练习

# 购物车程序项目：(20分钟)
# 要求：1、运行程序后，让用户输入支付宝余额，然后打印我们的商品列表给用户。
# 　　  2、让用户输入商品编号进行商品的购买。
# 　　  3、用户选择商品后，检查用户的余额是否够，若够则直接扣款，不够则提醒用户。
# 　　  4、用户可以随时退出购买，推出时打印用户已购买的商品和支付宝余额。

goods = [
    ["10001","python课本","88"],
    ["10002","蜜雪冰城—冰茶","10"],
    ["10003","iphone13 pro","9999"],
    ["10004","华为电-跑车","400000"],
    ["10005","小米手环","199"]
]
user_shop_list = []

支付宝余额 = input("请输入您的余额：")
info = '''------goods list-------
%s
%s
%s
%s
%s
'''%(goods[0],goods[1],goods[2],goods[3],goods[4])
print(info)
user_input_ID = input("请输入商品的ID：")
for good in goods:
    print(good)
    # 判断商品的id是否正确
    if user_input_ID == good[0]:
        # 判断用户的余额是否够用
        if int(good[2]) < int(支付宝余额):
            # 把商品加进list
            user_shop_list.append(good)
            # 扣除支付宝余额
            break

    else:
        print("您输入的商品信息有问题，请输入正确的商品ID")

print(user_shop_list)
