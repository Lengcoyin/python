# Author:keyin
# date:week6


# A.列表的基本方法

stu_id = [10001,10002,10003,10004,10008,10001,10009,10010,10001]
# 思考，如何取出所有位置10001的index？
names = ["Mike", "Mary", "Jan", "Jack"]

# 列表的私有方法

# 1.增加的方法
## 1.1 增加: append()  增加在list的末尾
# names = ["Mike","Mary","Jan","Jack"]
# names.append("Alex")
# print(names)


## 1.2 插入： insert() 可以指定位置增加元素
names.insert(0,"youge")
print("insert之后的names:",names)
names.insert(2,"youge")
print("insert两次之后的names:",names)


# 2. 删除: remove 和 pop
## 优势：如果删除list中多个元素时，remove比较合适
##
"""
Remove first occurrence of value.
Raises ValueError if the value is not present.
"""
## 2.1 remove()一般情况下 使用remove先用in做判断
# names = ['Mike', 'Mary', 'Jan', 'Jack', 'Alex']
# if "Alex" in names:
    # names.remove("Alex")
    # print("remove删除后的结果:",names)



## 2.2 pop() 删除位置为1的这个元素
# （pop()删除位置为1的这个元素）
# names = ['Mike', 'Mary', 'Jan', 'Jack', 'Alex']
# names.pop(1)
# print("pop()方法后的：",names)



## 3. index()索引 查看该元素如10001 在stu_id中第一个出现的位置索引
print(stu_id.index(10001))

## 4. clear()清除所有数据
# names.clear()
# print("清除names列表后的值：",names)

## 5.count()查看列表元素出现的个数，（简单应用）统计分数出现的次数
# print("count方法的结果:",stu_id.count(10001))
# print(names)

## 6. extend() 是给指定的list进行扩充
# names.extend(stu_id)
# print(names)



# 列表的其他方法(Sequence Types 的一些方法)
## 1. len()查看list长度
print("names的长度/names的列表元素个数：",len(names))
## 2. in 查看元素是否存在list当中,结果为布尔值，False/True,
##    一般在操作list的修改和删除时会先判断
print("keyin" in names)



#  B.列表的高级方法_copy
stu_id = [10001,10002,10003,10004,10008,10001,10009,10010,10001]

# 1. copy()很重要
# 思考，赋值是真正的复制么？ 赋值(=) <=> copy? 不等价
stu_id_matedata = stu_id
print("stu_id:",stu_id,'\n','stu_id_matedata:',stu_id_matedata)

# 实验 1 赋值
# stu_id.pop(1)
# print("stu_id:",stu_id,'\n','stu_id_matedata:',stu_id_matedata)

# 实验 2 copy()
# stu_id_matedata = stu_id.copy()
# stu_id.pop(1)
# print("stu_id:",stu_id,'\n','stu_id_matedata:',stu_id_matedata)

# 实验 3 切片实现复制
stu_id_matedata = stu_id[:]
stu_id.pop(1)
print("stu_id:",stu_id,'\n','stu_id_matedata:',stu_id_matedata)




#  C.列表的高级方法_枚举
stu_id = [10001,10002,10003,10004,10008,10001,10009,10010,10001]
# 思考，如何取出所有位置10001的index？
for i in stu_id:
    # 循环遍历stu_id的所有内容
    if i == 10001:
        # 判断如果元素为10001的时候,怎么取出索引值呢？
        print()
## 一般方法

# 枚举:因为list其实不仅有values值，还有index索引，但for循环主要循环遍历其值，不遍历索引
# 因此，有了枚举的方法，同时遍历两者
# enumerate()
pop_values_list = []  # append方法经常用于新建列表
for index,item in enumerate(stu_id):
    # print(index,item)
    if item == 10001:
        print(index,item)
        pop_values_list.append(index)
print("我们想要删除pop()的值：",pop_values_list)