from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NetWorkPage(BaseAction):
    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    click_first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def __init__(self, driver):
        super(NetWorkPage, self).__init__(driver)

    def click_normal_operation(self):
        self.find_element(self.more_button).click()
        self.driver.switch_to.default_content()
        self.driver.switch_to()
        self.driver.switch_to.window()
        self.driver.current_window_handle
        self.driver.current_url
        ActionChains(self.driver).move_to_element()
        self.click(self.more_button)
        self.click(self.mobile_network_button)

    def click_first_network(self):
        self.click(self.click_first_network_button)

    def click_2g(self):
        self.click(self.network_2g_button)

    def click_3g(self):
        self.click(self.network_3g_button)
