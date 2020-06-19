import allure
from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class SettingsPage(BasePage):
    settings_items = (MobileBy.CLASS_NAME, 'android.widget.RelativeLayout')
    currency_items = (MobileBy.CLASS_NAME, 'android.widget.CheckedTextView')

    @allure.step
    def change_currency_to_usd(self):
        self.driver.find_elements(*SettingsPage.settings_items)[1].click()
        self.driver.find_elements(*SettingsPage.currency_items)[1].click()

    @allure.step
    def hide_comments_section(self):
        self.driver.find_elements(*SettingsPage.settings_items)[6].click()

    @allure.step
    def hide_amount_section(self):
        self.driver.find_elements(*SettingsPage.settings_items)[5].click()
