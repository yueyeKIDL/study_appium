#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from appium import webdriver


def init_driver():
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


class Base:
    def __init__(self):
        self.driver = init_driver()
