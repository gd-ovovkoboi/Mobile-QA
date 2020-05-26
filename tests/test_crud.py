import pytest
import allure


@pytest.mark.usefixtures('driver_setup')
class TestShoppingList():

    @allure.title("A some test title")
    def test_shopping_list(self):
        pass
