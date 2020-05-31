import allure
import pytest

from pages.lists_page import ListsPage

LIST_NAME = 'grocery'
PRODUCT = {
    'name': 'cucumbers',
    'comments' : 'pickled',
    'price': 2,
    'amount': 3
}


@pytest.mark.usefixtures('driver_setup')
@allure.suite("Test Settings")
class TestSettings():

    @allure.title('Test currency')
    def test_currency(self):
        lists_page = ListsPage(self.driver)
        products_page = lists_page.add_list(LIST_NAME)
        products_page.add_product(PRODUCT)
        settings_page = products_page.open_settings()
        settings_page.change_currency_to_usd()
        settings_page.press_back_button()
        products_page.verify_currency('$')

    @allure.title('Test comments section')
    def test_comments_section(self):
        lists_page = ListsPage(self.driver)
        products_page = lists_page.add_list(LIST_NAME)
        products_page.add_product(PRODUCT)
        settings_page = products_page.open_settings()
        settings_page.hide_comments_section()
        settings_page.press_back_button()
        products_page.verify_comments_section_absence()

    @allure.title('Test amount section')
    def test_amount_section(self):
        lists_page = ListsPage(self.driver)
        products_page = lists_page.add_list(LIST_NAME)
        products_page.add_product(PRODUCT)
        settings_page = products_page.open_settings()
        settings_page.hide_amount_section()
        settings_page.press_back_button()
        products_page.verify_amount_section_absence()
