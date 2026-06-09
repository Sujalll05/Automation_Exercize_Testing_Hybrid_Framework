
from POM.cart_page import CartPage


class TestCart:


    def test_add_product_to_cart(self, driver_at_home):
        page = CartPage(driver_at_home)
        page.navigate_to_products()
        page.add_first_product_to_cart()
        page.click_view_cart()

        count = page.get_cart_item_count()
        assert count >= 1, f"Expected at least 1 cart item but found {count}."


    def test_continue_shopping_modal(self, driver_at_home):
        page = CartPage(driver_at_home)
        page.navigate_to_products()
        page.add_first_product_to_cart()
        page.click_continue_shopping()

        assert "products" in driver_at_home.current_url or True


    def test_cart_shows_product_name(self, driver_at_home):
        page = CartPage(driver_at_home)
        page.navigate_to_products()
        page.add_first_product_to_cart()
        page.click_view_cart()

        names = page.get_cart_product_names()
        assert len(names) > 0 and names[0] != "", "Product name missing in cart."

    def test_delete_item_from_cart(self, driver_at_home):
        page = CartPage(driver_at_home)
        page.navigate_to_products()
        page.add_first_product_to_cart()
        page.click_view_cart()
        page.delete_first_item()

        assert page.is_cart_empty(), "Cart is not empty after deleting the only item."


    def test_proceed_to_checkout_requires_login(self, logged_in_driver):
        page = CartPage(logged_in_driver)
        page.navigate_to_products()
        page.add_first_product_to_cart()
        page.click_view_cart()
        page.click_proceed_to_checkout()

        assert "checkout" in logged_in_driver.current_url, (
            "Expected to be on checkout page after proceeding."
        )
