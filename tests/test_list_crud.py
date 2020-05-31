import allure
import pytest

from pages.lists_page import ListsPage

LIST_NAME = 'grocery'
UPDATED_LIST_NAME = 'pharmacy'


@pytest.mark.usefixtures('driver_setup')
@allure.suite("Test List CRUD Suite")
class TestShoppingList():

    @allure.title('Add shopping list')
    def test_add_shopping_list(self):
        lists_page = ListsPage(self.driver)
        lists_page.add_list(LIST_NAME)
        lists_page.press_back_button()
        lists_page.verify_list_presence(LIST_NAME)

    @allure.title('Update shopping list')
    def test_update_shopping_list(self):
        lists_page = ListsPage(self.driver)
        lists_page.add_list(LIST_NAME)
        lists_page.press_back_button()
        lists_page.update_list(UPDATED_LIST_NAME)
        lists_page.verify_list_presence(UPDATED_LIST_NAME)

    @allure.title('Delete shopping list')
    def test_delete_shopping_list(self):
        lists_page = ListsPage(self.driver)
        lists_page.add_list(LIST_NAME)
        lists_page.press_back_button()
        lists_page.delete_list()
        lists_page.verify_list_absence()
