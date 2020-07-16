#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from appium import webdriver


def init_driver():
    # server 启动参数
    desired_caps = dict()

    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = 'Android Emulator'

    # app的信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'

    # 解决输入中文
    # desired_caps['unicodeKeyboard'] = True
    # desired_caps['resetKeyboard'] = True

    desired_caps['noReset'] = True
    desired_caps['chromedriverExecutable'] = r'F:\Python Projects\study_appium\chromedriver.exe'

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
