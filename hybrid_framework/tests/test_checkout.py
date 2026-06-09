"""
tests/test_checkout.py
Hybrid Framework — Checkout test suite
Covers: address visible, place order, full payment + order confirmation.
"""
from POM.cart_page import CartPage
from POM.checkout_page import CheckoutPage


class TestCheckout:

    def _add_product_and_go_to_checkout(self, driver):
        """Helper: add item, go to cart, proceed to checkout."""
        cart = CartPage(driver)
        cart.navigate_to_products()
        cart.add_first_product_to_cart()
        cart.click_view_cart()
        cart.click_proceed_to_checkout()

    # ── TC-CH-01: Address details visible on checkout page ───────────────────
    def test_address_details_visible(self, logged_in_driver):
        self._add_product_and_go_to_checkout(logged_in_driver)
        page = CheckoutPage(logged_in_driver)
        assert page.is_address_details_visible(), "Address Details section not visible on checkout."

    # ── TC-CH-02: Full order placement with payment ───────────────────────────
    def test_place_order_successfully(self, logged_in_driver, payment_data):
        self._add_product_and_go_to_checkout(logged_in_driver)
        page = CheckoutPage(logged_in_driver)
        p = payment_data[0]

        page.enter_order_comment("Automated test order — please ignore.")
        page.click_place_order()
        page.fill_payment_details(
            name      = p["Name_On_Card"],
            card_num  = p["Card_Number"],
            cvc       = p["CVC"],
            exp_month = p["Expiry_Month"],
            exp_year  = p["Expiry_Year"],
        )
        page.click_confirm_order()

        assert page.is_order_placed_successfully(), (
            "Order confirmation message not found — order may not have been placed."
        )

    # ── TC-CH-03: Data-driven payment with multiple cards ─────────────────────
    def test_payment_multiple_cards(self, logged_in_driver, payment_data):
        for idx, p in enumerate(payment_data):
            self._add_product_and_go_to_checkout(logged_in_driver)
            page = CheckoutPage(logged_in_driver)

            page.enter_order_comment(f"Card test row {idx}")
            page.click_place_order()
            page.fill_payment_details(
                name      = p["Name_On_Card"],
                card_num  = p["Card_Number"],
                cvc       = p["CVC"],
                exp_month = p["Expiry_Month"],
                exp_year  = p["Expiry_Year"],
            )
            page.click_confirm_order()

            assert page.is_order_placed_successfully(), (
                f"Order failed for payment row {idx}: card {p['Card_Number']}"
            )
