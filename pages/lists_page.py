import allure
from appium.webdriver.common.mobileby import MobileBy

from pages.header_page import HeaderPage
from pages.products_page import ProductsPage


class ListsPage(HeaderPage):
    text_box_list_name = (MobileBy.ID, 'com.slava.buylist:id/editText1')
    text_box_update_list_name = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    button_add_list = (MobileBy.ID, 'com.slava.buylist:id/button2')
    button_ok = (MobileBy.ID, 'android:id/button1')
    icons_list_actions = (MobileBy.CLASS_NAME, 'android.widget.ImageView')
    items_list = (MobileBy.ID, 'com.slava.buylist:id/title')

    @allure.step
    def add_list(self, list_name):
        self.driver.find_element(*ListsPage.text_box_list_name).send_keys(list_name)
        self.driver.find_element(*ListsPage.button_add_list).click()
        # hide keyboard
        self.press_back_button()
        return ProductsPage(self.driver)

    @allure.step
    def update_list(self, updated_list_name):
        self.driver.find_elements(*ListsPage.icons_list_actions)[1].click()
        self.wait_for_element(*ListsPage.text_box_update_list_name)
        self.driver.find_element(*ListsPage.text_box_update_list_name).clear()
        self.driver.find_element(*ListsPage.text_box_update_list_name).send_keys(updated_list_name)
        self.driver.find_element(*ListsPage.button_ok).click()

    @allure.step
    def delete_list(self):
        self.driver.find_elements(*ListsPage.icons_list_actions)[2].click()
        self.driver.find_element(*ListsPage.button_ok).click()

    @allure.step
    def verify_list_presence(self, list_name):
        assert list_name == self.driver.find_element(*ListsPage.items_list).text

    @allure.step
    def verify_list_absence(self):
        assert not self.driver.find_elements(*ListsPage.items_list)
