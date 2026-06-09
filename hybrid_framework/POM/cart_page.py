
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

WAIT_TIME = 10


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, WAIT_TIME)

    CART_LINK           = (By.XPATH, '//a[@href="/view_cart"]')
    PRODUCTS_LINK       = (By.XPATH, '//a[@href="/products"]')
    FIRST_ADD_TO_CART   = (By.XPATH, '(//a[@data-product-id])[1]')
    CONTINUE_SHOPPING   = (By.XPATH, '//button[contains(text(),"Continue Shopping")]')
    VIEW_CART_MODAL_BTN = (By.XPATH, '//u[contains(text(),"View Cart")]')
    CART_ITEMS          = (By.CLASS_NAME, "cart_product")
    PRODUCT_NAME_CART   = (By.XPATH, '//td[@class="cart_description"]//h4/a')
    PRODUCT_PRICE_CART  = (By.CLASS_NAME, "cart_price")
    PRODUCT_QTY_CART    = (By.CLASS_NAME, "cart_quantity")
    DELETE_BUTTON       = (By.XPATH, '(//a[@class="cart_quantity_delete"])[1]')
    EMPTY_CART_MSG      = (By.XPATH, '//b[contains(text(),"Cart is empty!")]')
    PROCEED_CHECKOUT    = (By.XPATH, '//a[contains(text(),"Proceed To Checkout")]')


    def _safe_click(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            elem.click()
        except ElementClickInterceptedException:

            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
            self.driver.execute_script("arguments[0].click();", elem)

    def navigate_to_products(self):
        self._safe_click(self.PRODUCTS_LINK)

    def add_first_product_to_cart(self):
        self._safe_click(self.FIRST_ADD_TO_CART)

    def click_continue_shopping(self):
        self._safe_click(self.CONTINUE_SHOPPING)

    def click_view_cart(self):
        self._safe_click(self.VIEW_CART_MODAL_BTN)

    def navigate_to_cart(self):
        self._safe_click(self.CART_LINK)

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_cart_product_names(self):
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME_CART))
        return [i.text for i in self.driver.find_elements(*self.PRODUCT_NAME_CART)]

    def delete_first_item(self):
        self._safe_click(self.DELETE_BUTTON)

    def is_cart_empty(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.EMPTY_CART_MSG))
            return True
        except Exception:
            return False

    def click_proceed_to_checkout(self):
        self._safe_click(self.PROCEED_CHECKOUT)
