#yy的课程表
user_data = "keyin"
password_data = "12345"
user_data_vip = "lingkeyin"
password_data_vip = "010203"

count = 3
while True:
    count -= 1
    # 用户输入数据
    username = input("请输入您的帐号：")
    password = input("请输入您的密码：")
    # 判断账号
    if username == user_data or user_data_vip:
        if password == password_data or password_data_vip:
            print("欢迎",username,"登陆系统使用！")
            break
        else:
            if count == 0:
                print("您已输入三次且三次都不正确，请五分钟后再输入")
                break
            else:
                print("您输入的账号或密码不正确，请重新输入，你还有",count,"次机会")
    else:
        if count == 0:
            print("您已输入三次且三次都不正确，请五分钟后再输入")
            break
        else:
            print("您输入的账号或密码不正确，请重新输入，你还有",count,"次机会")

# 普通用户
if username == user_data:
    if password == password_data:
        print("欢迎登入系统，您是普通用户，今天您可以查询五次哦")
        count = 5
        while True:
            count -= 1
            if count == 0:
                print("您已使用完今天五次的机会，请明天再来尝试吧")
                break
            else:
                print("您还有",count,"次机会输入")

                week_time = int(input("需要查询周几的课呢？"))
                import datetime
                time = datetime.datetime.today().weekday()
                if week_time == 1:
                    print("1-2乒乓球");
                    print("6-7写作训练");
                    print("8-9大英")
                elif week_time == 2:
                    print("8-9新媒体时代的新闻评论");
                    print("12-14毛概理论")
                elif week_time == 3:
                    print("1-2大英");
                    print("3-5融合新闻学")
                elif week_time == 4:
                    print("3-5python语言");
                    print("8-9毛概实践")
                elif week_time == 5:
                    print("3-5创业基础实践")
                elif week_time == 6:
                    print("过个美美周六")
                elif week_time == 7:
                    print("过个美美周日")
    else:
        if count == 0:
            print("您已使用完五次机会，请明天再来尝试")
            break
        else:
            print("您所输入的密码不正确，还有",count,"次机会输入哦")
else:
    print("账号输入不正确")
    break

# VIP用户
if username == user_data_vip:
    if password == password_data_vip:
        print("欢迎登入系统，您是VIP用户，今天你可以查询十次哦")
        count = 10
        while True:
            count -= 1
            if count == 0:
                print("您已使用完今天十次的机会，请明天再来尝试吧")
                break
            else:
                print("您还有",count,"次机会输入")

                week_time = int(input("需要查询周几的课呢？"))
                import datetime

                time = datetime.datetime.today().weekday()
                if week_time == 1:
                    print("1-2乒乓球");
                    print("6-7写作训练");
                    print("8-9大英")
                elif week_time == 2:
                    print("8-9新媒体时代的新闻评论");
                    print("12-14毛概理论")
                elif week_time == 3:
                    print("1-2大英");
                    print("3-5融合新闻学")
                elif week_time == 4:
                    print("3-5python语言");
                    print("8-9毛概实践")
                elif week_time == 5:
                    print("3-5创业基础实践")
                elif week_time == 6:
                    print("过个美美周六")
                elif week_time == 7:
                    print("过个美美周日")
    else:
        if count == 0:
            print("您已使用完十次机会，请明天再来尝试")
            break
        else:
            print("您所输入的密码不正确，还有", count, "次机会输入哦")
else:
    print("账号输入不正确")
    break





