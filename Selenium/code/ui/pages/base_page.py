import time

from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import BasePageLocators, MainPageLocators


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):

    locators = BasePageLocators()
    locators_main = MainPageLocators()
    url = 'https://education.vk.company/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
        self.is_opened()

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))
    
    def find_all(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def search(self, query):
        elem = self.find(self.locators.QUERY_LOCATOR_ID)
        elem.send_keys(query)
        go_button = self.find(self.locators.GO_BUTTON_LOCATOR)
        go_button.click()
        self.my_assert()

    def my_assert(self):
        assert 1 == 1

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def switch_to_new_window(self, original_window, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > len(original_window))
        
        new_window = [window for window in self.driver.window_handles 
                     if window not in original_window][0]
        self.driver.switch_to.window(new_window)

    def click_and_switch_to_new_window(self, locator, timeout=10):
        original_window = self.driver.current_window_handle
        self.click(locator, timeout)
        self.switch_to_new_window([original_window], timeout)
        return original_window
