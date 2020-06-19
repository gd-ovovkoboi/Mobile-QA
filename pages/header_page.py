import allure
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage
from pages.settings_page import SettingsPage


class HeaderPage(BasePage):
    button_menu = (MobileBy.ID, 'com.slava.buylist:id/button1')
    menu_actions = (MobileBy.ID, 'android:id/title')

    @allure.step
    def open_settings(self):
        self.driver.find_element(*HeaderPage.button_menu).click()
        self.driver.find_elements(*HeaderPage.menu_actions)[0].click()
        return SettingsPage(self.driver)
