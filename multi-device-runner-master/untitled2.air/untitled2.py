# -*- encoding=utf8 -*-
__author__ = "Administrator"
import random
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


from airtest.core.api import *


from airtest.core.api import connect_device


# dev1 = connect_device("Android://127.0.0.1:5037/024cb92de069cf68")  # 连上第一台手机
# dev2 = connect_device("Android://127.0.0.1:5037/00c3350389b0cca8")  # 第二台手机
# print(G.DEVICE_LIST)
poco = AndroidUiautomationPoco()
# set_current(1)

touch(Template(r"tpl1594607279347.png", record_pos=(0.014, -0.768), resolution=(1080, 1920)))
list = []
with open("test.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        list.append(line)
a = random.choice(list)

text(a)

# touch(Template(r"tpl1594527956952.png", record_pos=(0.001, 0.659), resolution=(1080, 1920)))
# poco("应用").click()


# set_current(0)



auto_setup(__file__)