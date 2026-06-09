from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME = 10


class ContactPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)

    CONTACT_US_LINK  = (By.XPATH, '//a[@href="/contact_us"]')
    GET_IN_TOUCH_HDR = (By.XPATH, '//h2[contains(text(),"Get In Touch")]')
    NAME_FIELD       = (By.XPATH, '//input[@data-qa="name"]')
    EMAIL_FIELD      = (By.XPATH, '//input[@data-qa="email"]')
    SUBJECT_FIELD    = (By.XPATH, '//input[@data-qa="subject"]')
    MESSAGE_FIELD    = (By.XPATH, '//textarea[@data-qa="message"]')
    SUBMIT_BUTTON    = (By.XPATH, '//input[@data-qa="submit-button"]')
    SUCCESS_MESSAGE  = (By.XPATH, '//div[contains(@class,"alert-success")]')
    HOME_BUTTON      = (By.XPATH, '//a[contains(text(),"Home")]')

    def navigate_to_contact(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTACT_US_LINK)).click()

    def is_contact_page_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.GET_IN_TOUCH_HDR))
            return True
        except Exception:
            return False

    def fill_contact_form(self, name, email, subject, message):
        self.wait.until(EC.visibility_of_element_located(self.NAME_FIELD)).send_keys(name)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.SUBJECT_FIELD).send_keys(subject)
        self.driver.find_element(*self.MESSAGE_FIELD).send_keys(message)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def accept_alert(self):
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def is_success_message_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
            return True
        except Exception:
            return False

    def get_success_message_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text
