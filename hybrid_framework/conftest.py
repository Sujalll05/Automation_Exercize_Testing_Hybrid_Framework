import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.XLUtils import read_data_as_dicts

BASE_URL  = "https://automationexercise.com"
LOGIN_URL = f"{BASE_URL}/login"

_HERE          = os.path.dirname(os.path.abspath(__file__))
_DATA          = os.path.join(_HERE, "test_data")

LOGIN_DATA_FILE   = os.path.join(_DATA, "login_data.xlsx")
REG_DATA_FILE     = os.path.join(_DATA, "registration_data.xlsx")
CONTACT_DATA_FILE = os.path.join(_DATA, "contact_data.xlsx")
PAYMENT_DATA_FILE = os.path.join(_DATA, "payment_data.xlsx")
SEARCH_DATA_FILE  = os.path.join(_DATA, "search_data.xlsx")
LOCATOR_FILE      = os.path.join(_DATA, "locators.xlsx")



@pytest.fixture(scope="function")
def driver():
    opt = Options()
    opt.add_argument("--start-maximized")

    _driver = webdriver.Chrome(options=opt)
    _driver.implicitly_wait(5)
    yield _driver
    _driver.quit()




@pytest.fixture(scope="function")
def driver_at_login(driver):
    driver.get(LOGIN_URL)
    return driver


@pytest.fixture(scope="function")
def driver_at_home(driver):
    driver.get(BASE_URL)
    return driver


@pytest.fixture(scope="function")
def logged_in_driver(driver_at_login, login_data):
    """Logs in with the first valid credential row, then yields the driver."""
    from POM.login_page import LoginPage
    user = login_data[0]
    LoginPage(driver_at_login).login(user["Username"], user["Password"])
    return driver_at_login



@pytest.fixture(scope="session")
def login_data():
    return read_data_as_dicts(LOGIN_DATA_FILE, "Sheet1")


@pytest.fixture(scope="session")
def registration_data():
    return read_data_as_dicts(REG_DATA_FILE, "Sheet1")


@pytest.fixture(scope="session")
def contact_data():
    return read_data_as_dicts(CONTACT_DATA_FILE, "Sheet1")


@pytest.fixture(scope="session")
def payment_data():
    return read_data_as_dicts(PAYMENT_DATA_FILE, "Sheet1")


@pytest.fixture(scope="session")
def search_data():
    return read_data_as_dicts(SEARCH_DATA_FILE, "Sheet1")
