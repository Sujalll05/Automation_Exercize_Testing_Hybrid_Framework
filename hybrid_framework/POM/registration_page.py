import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME = 10


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIME)


    SIGNUP_NAME     = (By.XPATH,  '//input[@data-qa="signup-name"]')
    SIGNUP_EMAIL    = (By.XPATH,  '//input[@data-qa="signup-email"]')
    SIGNUP_BTN      = (By.XPATH,  '//button[@data-qa="signup-button"]')
    GENDER_MALE     = (By.ID,     "id_gender1")
    PASSWORD        = (By.ID,     "password")
    DAY_SELECT      = (By.ID,     "days")
    MONTH_SELECT    = (By.ID,     "months")
    YEAR_SELECT     = (By.ID,     "years")
    NEWSLETTER      = (By.ID,     "newsletter")
    OPTIN           = (By.ID,     "optin")
    FIRST_NAME      = (By.ID,     "first_name")
    LAST_NAME       = (By.ID,     "last_name")
    COMPANY         = (By.ID,     "company")
    ADDRESS1        = (By.ID,     "address1")
    COUNTRY         = (By.ID,     "country")
    STATE           = (By.ID,     "state")
    CITY            = (By.ID,     "city")
    ZIPCODE         = (By.ID,     "zipcode")
    MOBILE          = (By.ID,     "mobile_number")
    CREATE_AC_BTN   = (By.XPATH,  '//button[@data-qa="create-account"]')
    ACCOUNT_CREATED = (By.XPATH,  '//b[contains(text(),"Account Created!")]')
    CONTINUE_BTN    = (By.XPATH,  '//a[@data-qa="continue-button"]')

#registration with valid credential
    def enter_signup_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.SIGNUP_NAME)).send_keys(name)

    def enter_signup_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.SIGNUP_EMAIL)).send_keys(email)

    def click_signup_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_BTN)).click()


    def select_gender(self):
        self.wait.until(EC.element_to_be_clickable(self.GENDER_MALE)).click()

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)

    def select_dob(self, day, month, year):
        Select(self.wait.until(EC.element_to_be_clickable(self.DAY_SELECT))).select_by_visible_text(day)
        Select(self.driver.find_element(*self.MONTH_SELECT)).select_by_visible_text(month)
        Select(self.driver.find_element(*self.YEAR_SELECT)).select_by_visible_text(year)

    def check_newsletter(self):
        self.wait.until(EC.element_to_be_clickable(self.NEWSLETTER)).click()

    def check_optin(self):
        self.wait.until(EC.element_to_be_clickable(self.OPTIN)).click()

    def enter_address_details(self, first, last, company, address, country, state, city, zipcode, mobile):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.COMPANY).send_keys(company)
        self.driver.find_element(*self.ADDRESS1).send_keys(address)
        Select(self.driver.find_element(*self.COUNTRY)).select_by_visible_text(country)
        self.driver.find_element(*self.STATE).send_keys(state)
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.ZIPCODE).send_keys(zipcode)
        self.driver.find_element(*self.MOBILE).send_keys(mobile)

    def click_create_account(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_AC_BTN)).click()

    def is_account_created(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_CREATED))
            return True
        except Exception:
            return False

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()

#one shot login once again
    def register(self, name, email, password, day, month, year,
                 first, last, company, address, country, state, city, zipcode, mobile):
        self.enter_signup_name(name)
        self.enter_signup_email(email)
        self.click_signup_button()
        self.select_gender()
        self.enter_password(password)
        self.select_dob(day, month, year)
        self.check_newsletter()
        self.check_optin()
        self.enter_address_details(first, last, company, address, country, state, city, zipcode, mobile)
        self.click_create_account()
