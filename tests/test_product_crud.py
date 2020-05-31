import allure
import pytest

from pages.lists_page import ListsPage

LIST_NAME = 'grocery'
PRODUCT = {
    'name': 'cucumbers',
    'comments': 'pickled',
    'price': 2,
    'amount': 3
}
UPDATED_PRODUCT = {
    'name': 'tomatoes',
    'comments': 'cherry',
    'price': 4,
    'amount': 5
}


@pytest.mark.usefixtures('driver_setup')
@allure.suite("Test Product CRUD Suite")
class TestProductCrud():

    @allure.title('Add product')
    def test_add_product(self):
        lists_page = ListsPage(self.driver)
        products_page = lists_page.add_list(LIST_NAME)
        products_page.add_product(PRODUCT)
        products_page.verify_product_presence(PRODUCT)

    @allure.title('Update product')
    def test_update_product(self):
        lists_page = ListsPage(self.driver)
        products_page = lists_page.add_list(LIST_NAME)
        products_page.add_product(PRODUCT)
        products_page.update_product(UPDATED_PRODUCT)
        products_page.verify_product_presence(UPDATED_PRODUCT)

    @allure.title('Delete product')
    def test_delete_product(self):
        lists_page = ListsPage(self.driver)
        products_page = lists_page.add_list(LIST_NAME)
        products_page.add_product(PRODUCT)
        products_page.delete_product()
        products_page.verify_product_absence()

    @allure.title('Verify totals calculation')
    def test_totals(self):
        lists_page = ListsPage(self.driver)
        products_page = lists_page.add_list(LIST_NAME)
        products_page.add_product(PRODUCT)
        products_page.add_product(UPDATED_PRODUCT)
        products_page.verify_totals([PRODUCT, UPDATED_PRODUCT])
