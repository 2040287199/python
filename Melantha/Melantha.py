#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

from pip._vendor.distlib.compat import raw_input

localtime = time.asctime(time.localtime(time.time()))
nian = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
shi = time.strftime("%Y-%m-%d %H:%M", time.localtime())

import datetime

time = datetime.datetime.now().weekday() + 1

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
        raw_input("(Enter 继续查看 /N 关闭)")
        print()
        f2 = open('text/生日2.txt', 'r', encoding='UTF-8')
        happy2 = f2.read()
        print(shi, "Melantha:")
        print(happy2)
        f2.close()

        # 生日3
        raw_input("(Enter 继续查看 /N 关闭)")
        print()
        f3 = open('text/生日3.txt', 'r', encoding='UTF-8')
        happy3 = f3.read()
        print(shi, "Melantha:")
        print(happy3,)
        f3.close()

        # 生日4
        raw_input("(Enter 继续查看 /N 关闭)")
        print()
        f4 = open('text/生日4.txt', 'r', encoding='UTF-8')
        happy4 = f4.read()
        print(shi, "Melantha:")
        print(happy4)
        f4.close()

        # 生日5
        raw_input("(Enter 继续查看 /N 关闭)")
        print()
        f5 = open('text/生日5.txt', 'r', encoding='UTF-8')
        happy5 = f5.read()
        print(shi, "Melantha:")
        print(happy5)
        f5.close()

        # 生日6
        raw_input("(Enter 继续查看 /N 关闭)")
        print()
        f6 = open('text/生日6.txt', 'r', encoding='UTF-8')
        happy6 = f6.read()
        print(shi, "Melantha:")
        print(happy6)
        f6.close()

        # 生日7
        raw_input("(Enter 继续查看 /N 关闭)")
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
