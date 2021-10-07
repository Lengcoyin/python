# Author;KEYIN
# date:week5
# 主要知识: 列表入门

# 1.用户输入和格式化打印

# name = input("name: ")
# age = input("age: ")
# job = input("job: ")
# salary = input("salary: ")

# name 动态的出现在字符串中，字符串的拼接用"+" 符号来拼接
# info = '''----------INFO'''+ name+'''---------
# name:'''+name+'''
# age:'''+age+'''
# job:'''+job+'''
# salary:'''+salary
#

# print(info)

# 优化字符串拼接 ：  占位符 %s动态的数据----变量
# 优势： 1.全部都写在一个大的字符串里面了
#       2.省略了 "+" 符号
# 缺点？如果有几百个需要填进去的内容？容易顺序乱掉！出现打印结果的不正确
# 优化：  .format() 格式化 字符串

# name 动态的出现在字符串中
info_占位符 =  '''--------------INFO {姓名}---------
name:{姓名}
age:{年龄}
job:{工作}
salary:{薪水}''' .format(姓名=name,年龄=age,工作=job,薪水=salary)

print(info_format)

# .format() 案例

url = "https://www.nfu,edu.cn/"  #官网的域名
# 目标获取高教动态的所有url链接
高教动态 = "gjdt"
url_页面 = ".htm"
url_页面细节不变 = "/index"

for i in range(1,27):
    完整的高教动态所有页面url = "https://www.nfu.edu.cn/{新闻}/index{页码}.htm".format(页码=str(i), 新闻="ztb")
    print(完整的高教动态所有页面url)



    # 主要知识： 列表入门

    # 2.数据结构之列表

    user_data = "yy||kk||jj||pp"
    print(user_data[1])

    # 引入列表
    user_data_list = [["yy", 123456, 19], ["kk", 010203, 23], ["jj", boxbox, 25], ["pp", blueblue, 27]]
    # password_list = [123456,010203,boxbox,blueblue]
    # age = [19,23,25,27]
    # 1. 从左往右取值（index & slice）
    print(user_data_list[2])
    # 切片 slice ，右边的值取不到 例如[0:3] 索引为3的值取不到
    print(user_data_list[0:3])
    # 当从0开始取值时，0 可以忽略不写
    print(user_data_list[:3])

    # -3，-2，-1，0，1，2，3，4..
    # 2. 从右往左取值(index & slice)
    print(user_data_list[-2])
    # 切片 slice ，右边的值取不到 例如[-3:-1] 索引为-1的值取不到
    print(user_data_list[-3:-1])
    # 如果取值为空：说明slice写错了 例如[-3:0]
    # 如果要取到最后一个值，不能写0，直接省略不写
    print(user_data_list[-3:0])
    print(user_data_list[-3:])

    # ****重要****
    print(user_data_list[:])

    # 步长，list列表slice ：[start:stop:step]
    '''
    如果没有指定开始值，则默认为0；
    如果没有指定结束指，则取列表允许的最大值；
    如果没有指定步长值，则默认步长为1.
    '''
    num = list(range(10))
    print(num)
    print(num[0:6:2])

    Q = squares + [36, 39, 49, 64, 81, 100]
    print(Q)