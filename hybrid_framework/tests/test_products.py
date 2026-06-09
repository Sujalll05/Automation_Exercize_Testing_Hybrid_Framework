"""
tests/test_products.py
Hybrid Framework — Products test suite
Covers: page visibility, product count, product detail view, search.
"""
import pytest
from POM.product_page import ProductsPage


class TestProducts:

    # ── TC-P-01: Products page loads ─────────────────────────────────────────
    def test_products_page_is_visible(self, driver_at_home):
        page = ProductsPage(driver_at_home)
        page.navigate_to_products()
        assert page.is_products_page_visible(), "'All Products' header not visible."

    # ── TC-P-02: Product list is not empty ───────────────────────────────────
    def test_products_list_is_not_empty(self, driver_at_home):
        page = ProductsPage(driver_at_home)
        page.navigate_to_products()
        count = page.get_product_count()
        assert count > 0, f"Expected at least 1 product but found {count}."

    # ── TC-P-03: View first product detail ───────────────────────────────────
    def test_view_first_product_details(self, driver_at_home):
        page = ProductsPage(driver_at_home)
        page.navigate_to_products()
        page.click_first_product()

        name  = page.get_product_name()
        price = page.get_product_price()

        assert name  != "", "Product name is empty on detail page."
        assert price != "", "Product price is empty on detail page."

    # ── TC-P-04: Data-driven search ──────────────────────────────────────────
    @pytest.mark.parametrize("keyword", ["Top", "Dress", "Jean"])
    def test_search_returns_results(self, driver_at_home, keyword):
        page = ProductsPage(driver_at_home)
        page.navigate_to_products()
        page.search_product(keyword)

        results = page.get_search_results()
        assert len(results) > 0, f"Search for '{keyword}' returned no results."

    # ── TC-P-05: Data-driven search from Excel ────────────────────────────────
    def test_search_from_excel_data(self, driver_at_home, search_data):
        page = ProductsPage(driver_at_home)

        for row in search_data:
            driver_at_home.refresh()
            page.navigate_to_products()
            page.search_product(row["Keyword"])
            results = page.get_search_results()
            assert len(results) > 0, f"No results for keyword: {row['Keyword']}"
