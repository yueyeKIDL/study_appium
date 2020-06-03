#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import Base


class Display(Base):

    def click_display_button(self):
        display_button = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath("//*[@content-desc='搜索']"))
        display_button.click()
        print(1, self.driver)

    def input_search_content(self, item):
        search_content = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath("//*[contains(@text,'搜索')]"))
        search_content.send_keys(item)
        print(2, self.driver)

    def click_back_button(self):
        back_button = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath("//*[@content-desc='收起']"))
        back_button.click()
        print(3, self.driver)
