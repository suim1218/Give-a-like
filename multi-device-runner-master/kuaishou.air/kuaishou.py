# -*- encoding=utf8 -*-
# 免责声明：
# 本代码（multi-device-runner-master）仅限用于学习和研究目的；不得将上述内容用于商业或者非法用途，否则，一切后果请用户自负。代码内容来自网络，版权争议与本人无关。您必须在下载后的24个小时之内，从您的电脑中彻底删除上述内容。如果您喜欢该程序，请支持正版软件，购买注册，得到更好的正版服务。
__author__ = "Administrator"

from airtest.core.api import *

import random
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from airtest.core.api import connect_device

# dev1 = connect_device("Android://127.0.0.1:5037/024cb92de069cf68")  # 连上第一台手机
# dev2 = connect_device("Android://127.0.0.1:5037/00c3350389b0cca8")  # 第二台手机
# print(G.DEVICE_LIST)
poco = AndroidUiautomationPoco()
# set_current(1)

poco("com.smile.gifmaker:id/right_btn").click()
# touch(Template(r"tpl1594630229475.png", record_pos=(0.431, -0.967), resolution=(1080, 2400)))
poco("com.smile.gifmaker:id/search_layout").click()

list = []
with open("test.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        list.append(line)
# a = random.choice(list)
sum = 0
while sum < 10:
    if poco('com.smile.gifmaker:id/clear_button').exists():
        poco("com.smile.gifmaker:id/clear_button").click()
        # text("1212869517")
        sleep(0.5)
        text(random.choice(list))
        sleep(0.5)
    else:
        text(random.choice(list))
        # text("1212869517")
        sleep(0.5)
    # text(i)
    # 点击搜索
    poco("com.smile.gifmaker:id/right_tv").click()
    # touch(Template(r"tpl1594630300020.png", record_pos=(0.419, -0.943), resolution=(1080, 2400)))
    sleep(0.2)
    # 点击第一个视频
    if poco(name='com.smile.gifmaker:id/container').exists():
        poco(name='com.smile.gifmaker:id/container').click()
        sleep(0.3)
        value = poco("com.smile.gifmaker:id/like_button").attr('selected')
        if value == False:
            sleep(1)
            poco(name='com.smile.gifmaker:id/like_button').click()
            poco(name='com.smile.gifmaker:id/back_btn').click()
        else:
            poco(name='com.smile.gifmaker:id/back_btn').click()
    else:
        poco("com.smile.gifmaker:id/left_btn").click()
    sum += 1
poco("com.smile.gifmaker:id/left_btn").click()
sleep(0.3)
poco("com.smile.gifmaker:id/left_btn").click()
poco("com.smile.gifmaker:id/left_btn").click()
sleep(0.3)
poco("com.smile.gifmaker:id/tab_avatar_wrapper").click()
sleep(0.3)
poco("com.smile.gifmaker:id/profile_settings_button").click()
poco("com.smile.gifmaker:id/intro_layout").click()
sleep(0.3)
poco("com.smile.gifmaker:id/input").set_text("")
text("131011009")
poco("com.smile.gifmaker:id/right_btn").click()

'''
for i in list:
    poco("com.smile.gifmaker:id/search_layout").click()
    if poco('com.smile.gifmaker:id/clear_button').exists():
        poco("com.smile.gifmaker:id/clear_button").click()
        text(i)
    else:
        text(i)
    # text(i)
    # 点击搜索
    poco("com.smile.gifmaker:id/right_tv").click()
    # touch(Template(r"tpl1594630300020.png", record_pos=(0.419, -0.943), resolution=(1080, 2400)))
    sleep(1.0)
    # 点击第一个视频
    if poco(name='com.smile.gifmaker:id/container').exists():
        poco(name='com.smile.gifmaker:id/container').click()
        sleep(1.0)
        value = poco("com.smile.gifmaker:id/like_button").attr('selected')
        if value == False:
            poco(name='com.smile.gifmaker:id/like_button').click()
            poco(name='com.smile.gifmaker:id/back_btn').click()
        else:
            poco(name='com.smile.gifmaker:id/back_btn').click()
    else:
        poco("com.smile.gifmaker:id/left_btn").click()
    # sleep(1.0)
    # value = poco("com.smile.gifmaker:id/like_button").attr('selected')
    # if value == False:
    #     poco(name='com.smile.gifmaker:id/like_button').click()
    #     poco(name='com.smile.gifmaker:id/back_btn').click()
    # else:
    #     poco(name='com.smile.gifmaker:id/back_btn').click()
'''
auto_setup(__file__)
