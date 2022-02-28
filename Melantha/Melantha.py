#!/usr/bin/python
# -*- coding: UTF-8 -*-
    """
    下载这个py文件要下载上面的text文档
    我不知道这个代码我写的意义在哪就算是练习吧
    Melantha名字自然是我喜欢某个游戏的女性角色英文名
    emmm就算这个代码是每天提醒你该干什么事的管家吧（大概）把代码创建快捷方式丢到开机启动里
    每天开机后就能看到今天你要做什么事情，类似于便签吧没什么卵用，他的任务就是打开text/...的txt文件把里面的所有记录的内容展现出来
    
    例如今天星期一，Genshin周本更新
    这时你把文件丢到开机启动里，只要你打开电脑了他会弹出以下对话框内容
    {
    
    2022-02-28 09:21:06 星期一
    Genshin game:
    天赋本
    自由  繁荣  浮世
    
    武器素材
    高塔孤王的破瓦
    孤云寒林的光砂
    远海一地的珊枝
    
    }
    
    你可以拿去写写特殊事件例如你的生日事件：
    
    {
    2022-02-28 09:26:01
    来自你的程序Melantha邀请你通话:(Enter 查看)

    2022-02-28 09:26 Melantha:
    今天是你的生日你就不想做点什么嘛？
    比如出门逛逛街什么的，你不能一天到晚都宅在家里啊！！
    (Enter 继续查看)
    ......
    
    }
    当然你要想写情人节事件之类的也不是不可以，时间问题
    好吧，也许是个无聊的程序
    
    以后更新第一回启动输入生日之类的事件，让你感受 船 新 体 验 ！
    
    
    
    """

import time

from pip._vendor.distlib.compat import raw_input

localtime = time.asctime(time.localtime(time.time()))
nian = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
shi = time.strftime("%Y-%m-%d %H:%M", time.localtime())

import datetime

time = datetime.datetime.now().weekday() + 1

#每日提醒文件内容

if time == 1:
    print(nian, '星期一')
    f1 = open("text/星期一.txt", 'r', encoding='UTF-8')
    text = f1.read()
    print(text)
    f1.close()

elif time == 2:
    print(nian, '星期二')
    f1 = open("text/星期二.txt", 'r', encoding='UTF-8')
    text = f1.read()
    print(text)
    f1.close()

elif time == 3:
    print(nian, '星期三')
    f1 = open("text/星期三.txt", 'r', encoding='UTF-8')
    text = f1.read()
    print(text)
    f1.close()
elif time == 4:
    print(nian, '星期四')
    f1 = open("text/星期四.txt", 'r', encoding='UTF-8')
    text = f1.read()
    print(text)
    f1.close()

elif time == 5:
    print(nian, '星期五')
    f1 = open("text/星期五.txt", 'r', encoding='UTF-8')
    text = f1.read()
    print(text)
    f1.close()

elif time == 6:
    print(nian, '星期六')
    f1 = open("text/星期六.txt", 'r', encoding='UTF-8')
    text = f1.read()
    print(text)
    f1.close()

elif time == 7:
    print(nian, '星期日')
    f1 = open("text/星期日.txt", 'r', encoding='UTF-8')
    text = f1.read()
    print(text)
    f1.close()
else:
    print('0')


# 生日检测
def is_today(target_date):
    """
    这个程序时自动检测的当然你要输入你的生日is_today('2022-2-6')
    把括号里的数字改了就行
    生日对话文件在/text文件夹里想改的话可以到里面找txt文件慢慢改

    """
    c_month = datetime.datetime.now().month
    c_day = datetime.datetime.now().day

    date_list = target_date.split(" ")[0].split("-")
    t_month = int(date_list[0])
    t_day = int(date_list[1])

    if  c_month == t_month and c_day == t_day:
        print(nian)
        # 生日1
        raw_input("来自你的程序Melantha邀请你通话:(Enter 查看 /N 关闭)")
        print()
        f1 = open('text/生日1.txt', 'r', encoding='UTF-8')
        happy = f1.read()
        print(shi, "Melantha:")
        print(happy)
        f1.close()

        # 生日2
        raw_input("(Enter 继续查看)")
        print()
        f2 = open('text/生日2.txt', 'r', encoding='UTF-8')
        happy2 = f2.read()
        print(shi, "Melantha:")
        print(happy2)
        f2.close()

        # 生日3
        raw_input("(Enter 继续查看")
        print()
        f3 = open('text/生日3.txt', 'r', encoding='UTF-8')
        happy3 = f3.read()
        print(shi, "Melantha:")
        print(happy3,)
        f3.close()

        # 生日4
        raw_input("(Enter 继续查看)")
        print()
        f4 = open('text/生日4.txt', 'r', encoding='UTF-8')
        happy4 = f4.read()
        print(shi, "Melantha:")
        print(happy4)
        f4.close()

        # 生日5
        raw_input("(Enter 继续查看)")
        print()
        f5 = open('text/生日5.txt', 'r', encoding='UTF-8')
        happy5 = f5.read()
        print(shi, "Melantha:")
        print(happy5)
        f5.close()

        # 生日6
        raw_input("(Enter 继续查看)")
        print()
        f6 = open('text/生日6.txt', 'r', encoding='UTF-8')
        happy6 = f6.read()
        print(shi, "Melantha:")
        print(happy6)
        f6.close()

        # 生日7
        raw_input("(Enter 继续查看)")
        print()
        f7 = open('text/生日7.txt', 'r', encoding='UTF-8')
        happy7 = f7.read()
        print(shi, "Melantha:")
        print(happy7)
        f7.close()

        print('通讯似乎已经结束了')
        input('(点击任意键关闭通讯)')


is_today('2-28')

input("点击任意键关闭")
