import time

from selenium.common.exceptions import StaleElementReferenceException

KEY_CODE_BACK = 4


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def press_back_button(self):
        self.driver.keyevent(KEY_CODE_BACK)

    def wait_for_element(self, by, locator):
        for i in range(5):
            try:
                self.driver.find_element(by, locator)
                break
            except StaleElementReferenceException:
                time.sleep(1)
