import allure
from appium.webdriver.common.mobileby import MobileBy

from pages.header_page import HeaderPage


class ProductsPage(HeaderPage):
    text_box_product_name = (MobileBy.ID, 'com.slava.buylist:id/editText1')
    text_box_product_price = (MobileBy.ID, 'com.slava.buylist:id/editText2')
    text_box_product_amount = (MobileBy.ID, 'com.slava.buylist:id/editText3')
    text_box_product_comments = (MobileBy.ID, 'com.slava.buylist:id/editText4')
    text_box_update_list_name = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    button_add_product = (MobileBy.ID, 'com.slava.buylist:id/button2')
    product_title = (MobileBy.ID, 'com.slava.buylist:id/title')
    product_amount = (MobileBy.ID, 'com.slava.buylist:id/TextView01')
    product_price = (MobileBy.ID, 'com.slava.buylist:id/textView1')
    product_comments = (MobileBy.ID, 'com.slava.buylist:id/str1')
    product_actions = (MobileBy.ID, 'android:id/title')
    button_ok = (MobileBy.ID, 'android:id/button1')
    totals = (MobileBy.ID, 'com.slava.buylist:id/textView2')

    @allure.step
    def add_product(self, product):
        self.wait_for_element(*ProductsPage.text_box_product_name)
        self.driver.find_element(*ProductsPage.text_box_product_name).send_keys(product['name'])
        self.wait_for_element(*ProductsPage.text_box_product_price)
        self.driver.find_element(*ProductsPage.text_box_product_price).send_keys(product['price'])
        self.driver.find_element(*ProductsPage.text_box_product_amount).send_keys(product['amount'])
        self.driver.find_element(*ProductsPage.text_box_product_comments).send_keys(product['comments'])
        self.driver.find_element(*ProductsPage.button_add_product).click()

    @allure.step
    def update_product(self, product):
        self.wait_for_element(*ProductsPage.text_box_product_name)
        self.long_press(self.driver, self.driver.find_element(*ProductsPage.product_title))
        self.driver.find_elements(*ProductsPage.product_actions)[2].click()
        self.wait_for_element(*ProductsPage.text_box_product_name)
        self.driver.find_element(*ProductsPage.text_box_product_name).clear()
        self.driver.find_element(*ProductsPage.text_box_product_name).send_keys(product['name'])
        self.driver.find_element(*ProductsPage.text_box_product_price).clear()
        self.driver.find_element(*ProductsPage.text_box_product_price).send_keys(product['price'])
        self.driver.find_element(*ProductsPage.text_box_product_amount).clear()
        self.driver.find_element(*ProductsPage.text_box_product_amount).send_keys(product['amount'])
        self.driver.find_element(*ProductsPage.text_box_product_comments).clear()
        self.driver.find_element(*ProductsPage.text_box_product_comments).send_keys(product['comments'])
        self.driver.find_element(*ProductsPage.button_add_product).click()

    @allure.step
    def delete_product(self):
        self.long_press(self.driver, self.driver.find_element(*ProductsPage.product_title))
        self.driver.find_elements(*ProductsPage.product_actions)[3].click()
        self.driver.find_element(*ProductsPage.button_ok).click()

    @allure.step
    def verify_product_presence(self, product):
        assert product['name'] == self.driver.find_element(*ProductsPage.product_title).text
        assert str(product['comments']) == self.driver.find_element(*ProductsPage.product_comments).text
        assert str(product['price']) in self.driver.find_elements(*ProductsPage.product_price)[1].text
        assert str(product['amount']) in self.driver.find_element(*ProductsPage.product_amount).text

    @allure.step
    def verify_product_absence(self):
        assert not self.driver.find_elements(*ProductsPage.product_title)

    @allure.step
    def verify_currency(self, currency):
        assert currency in self.driver.find_elements(*ProductsPage.product_price)[1].text

    @allure.step
    def verify_comments_section_absence(self):
        assert not self.driver.find_elements(*ProductsPage.product_comments)

    @allure.step
    def verify_amount_section_absence(self):
        assert not self.driver.find_elements(*ProductsPage.product_amount)

    @allure.step
    def verify_totals(self, products_list):
        total = 0
        for product in products_list:
            total += product['amount'] * product['price']
        assert str(total) in self.driver.find_element(*ProductsPage.totals).text
