from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME = 10


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    PROCEED_TO_CHECKOUT  = (By.XPATH, '//a[contains(text(),"Proceed To Checkout")]')
    DELIVERY_ADDRESS_HDR = (By.XPATH, '//h3[contains(text(),"Address Details")]')
    ORDER_COMMENT        = (By.XPATH, '//textarea[contains(@name,"message")]')
    PLACE_ORDER_BTN      = (By.XPATH, '//a[contains(text(),"Place Order")]')
    NAME_ON_CARD         = (By.XPATH, '//input[@data-qa="name-on-card"]')
    CARD_NUMBER          = (By.XPATH, '//input[@data-qa="card-number"]')
    CVC                  = (By.XPATH, '//input[@data-qa="cvc"]')
    EXPIRY_MONTH         = (By.XPATH, '//input[@data-qa="expiry-month"]')
    EXPIRY_YEAR          = (By.XPATH, '//input[@data-qa="expiry-year"]')
    CONFIRM_ORDER_BTN    = (By.XPATH, '//button[@data-qa="pay-button"]')
    ORDER_SUCCESS_MSG    = (By.XPATH, '//b[contains(text(),"Order Placed!")]')
    ORDER_PLACED_ALT     = (By.XPATH, '//p[contains(text(),"Congratulations")]')

    def click_proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.PROCEED_TO_CHECKOUT)).click()

    def is_address_details_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.DELIVERY_ADDRESS_HDR))
            return True
        except Exception:
            return False

    def enter_order_comment(self, comment):
        self.wait.until(EC.visibility_of_element_located(self.ORDER_COMMENT)).send_keys(comment)

    def click_place_order(self):
        self.wait.until(EC.element_to_be_clickable(self.PLACE_ORDER_BTN)).click()

    def fill_payment_details(self, name, card_num, cvc, exp_month, exp_year):
        self.wait.until(EC.visibility_of_element_located(self.NAME_ON_CARD)).send_keys(name)
        self.driver.find_element(*self.CARD_NUMBER).send_keys(card_num)
        self.driver.find_element(*self.CVC).send_keys(cvc)
        self.driver.find_element(*self.EXPIRY_MONTH).send_keys(exp_month)
        self.driver.find_element(*self.EXPIRY_YEAR).send_keys(exp_year)

    def click_confirm_order(self):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_ORDER_BTN)).click()

    def is_order_placed_successfully(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ORDER_SUCCESS_MSG))
            return True
        except Exception:
            try:
                self.wait.until(EC.visibility_of_element_located(self.ORDER_PLACED_ALT))
                return True
            except Exception:
                return False
