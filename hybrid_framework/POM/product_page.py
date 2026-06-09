
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

WAIT_TIME = 10


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, WAIT_TIME)

    PRODUCTS_LINK       = (By.XPATH, '//a[@href="/products"]')
    ALL_PRODUCTS_HEADER = (By.XPATH, '//h2[contains(text(),"All Products")]')
    PRODUCT_LIST        = (By.CLASS_NAME, "product-image-wrapper")
    FIRST_VIEW_PRODUCT  = (By.XPATH, '(//a[contains(text(),"View Product")])[1]')
    PRODUCT_NAME        = (By.XPATH, '//div[@class="product-information"]//h2')
    PRODUCT_CATEGORY    = (By.XPATH, '//div[@class="product-information"]//p[1]')
    PRODUCT_PRICE       = (By.XPATH, '//div[@class="product-information"]//span/span')
    SEARCH_INPUT        = (By.ID, "search_product")
    SEARCH_BUTTON       = (By.ID, "submit_search")
    SEARCHED_PRODUCTS   = (By.XPATH, '//div[@class="productinfo text-center"]//p')

    def _safe_click(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            elem.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
            self.driver.execute_script("arguments[0].click();", elem)

    def navigate_to_products(self):
        self._safe_click(self.PRODUCTS_LINK)

    def is_products_page_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ALL_PRODUCTS_HEADER))
            return True
        except Exception:
            return False

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_LIST))

    def click_first_product(self):
        self._safe_click(self.FIRST_VIEW_PRODUCT)

    def get_product_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME)).text

    def get_product_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE)).text

    def search_product(self, keyword: str):
        """
        Navigate to /products first if not already there, then search.
        Handles the case where an ad reload caused the search box to vanish.
        """
        if "/products" not in self.driver.current_url:
            self.navigate_to_products()
        # Wait for page to settle before interacting with search
        self.wait.until(EC.visibility_of_element_located(self.ALL_PRODUCTS_HEADER))
        field = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        field.clear()
        field.send_keys(keyword)
        self._safe_click(self.SEARCH_BUTTON)

    def get_search_results(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCHED_PRODUCTS))
        return [i.text for i in self.driver.find_elements(*self.SEARCHED_PRODUCTS)]
