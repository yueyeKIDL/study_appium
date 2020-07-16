from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class BaseAction:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, loc, timeout=10, poll_frequency=0.5) -> WebElement:
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=10, poll_frequency=0.5) -> WebElement:
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        self.find_element(loc).send_keys(text)
