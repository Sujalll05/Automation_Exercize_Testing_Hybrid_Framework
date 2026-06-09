import openpyxl
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.XLUtils import read_locators

WAIT_TIME    = 10
LOCATOR_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "..", "test_data", "locators.xlsx")
SHEET = "Login"

BY_MAP = {
    "xpath":      By.XPATH,
    "id":         By.ID,
    "name":       By.NAME,
    "class_name": By.CLASS_NAME,
    "css":        By.CSS_SELECTOR,
    "link_text":  By.LINK_TEXT,
}

def _by(loc_type: str):
    return BY_MAP[loc_type.lower()]


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, WAIT_TIME)
        self._loc   = read_locators(LOCATOR_FILE, SHEET)

    def _find(self, component: str):
        t, v = self._loc[component]
        return self.wait.until(EC.visibility_of_element_located((_by(t), v)))

    def _click(self, component: str):
        t, v = self._loc[component]
        self.wait.until(EC.element_to_be_clickable((_by(t), v))).click()

    def enter_email(self, email: str):
        field = self._find("Email_txt_field"); field.clear(); field.send_keys(email)

    def enter_password(self, password: str):
        field = self._find("Password_txt_field"); field.clear(); field.send_keys(password)

    def click_login(self):
        self._click("Login_btn")

    def login(self, email: str, password: str):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self) -> bool:
        try:
            t, v = self._loc["Logged_in_user"]
            self.wait.until(EC.visibility_of_element_located((_by(t), v)))
            return True
        except Exception:
            return False

    def get_error_message(self) -> str:
        try:
            t, v = self._loc["Error_message"]
            return self.wait.until(EC.visibility_of_element_located((_by(t), v))).text
        except Exception:
            return ""

    def is_logout_visible(self) -> bool:
        try:
            t, v = self._loc["Logout_link"]
            self.wait.until(EC.visibility_of_element_located((_by(t), v)))
            return True
        except Exception:
            return False

    def click_logout(self):
        self._click("Logout_link")
