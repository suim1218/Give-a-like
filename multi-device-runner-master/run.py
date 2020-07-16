# -*- encoding=utf-8 -*-
# Run Airtest in parallel on multi-device
import os
import traceback
import subprocess
import getpass
from airtest.core.android.adb import ADB


def run(devices, air, run_all=False):
    try:
        tasks = run_on_multi_device(devices, air, run_all)
        for task in tasks:
            task['process'].wait()
    except Exception as e:
        traceback.print_exc()


def run_on_multi_device(devices, air, run_all):
    tasks = []
    for dev in devices:
        if (not run_all):
            print("Skip device %s" % dev)
            continue
        cmd = [
            "airtest","run",air,
            "--device",
            "Android:///" + dev
        ]
        try:
            tasks.append({
                'process': subprocess.Popen(cmd, cwd=os.getcwd()),
                'dev': dev,
                'air': air
            })
        except Exception as e:
            traceback.print_exc()
    return tasks


if __name__ == '__main__':
    login_result = False
    while login_result == False:
        username = input('请输入用户名:')
        password = getpass.getpass('请输入密码:')
        if username == "admin" and password=="123456":
            login_result = True
        else:
            print("用户名密码错误")
    print('Login Success!')
    devices = [tmp[0] for tmp in ADB().devices()]
    air = 'kuaishou.air'
    # 重新运行所有脚本
    run(devices, air, run_all=True)
