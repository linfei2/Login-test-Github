import os
from selenium.webdriver.common.by import By

# Main page locators
SIGN_IN_BTN = (By.XPATH, "//a[@href='/login']")

# Login page locators
USERNAME_FIELD = (By.ID, "login_field")
PASSWORD_FIELD = (By.ID, "password")
SUBMIT_BTN = (By.NAME, "commit")
ERROR_BOX = (By.XPATH, "//div[@class='container-lg px-2']")

# Inputs
URL = "https://github.com"
VALID_USERNAME = os.environ.get("LOGIN")
VALID_PASSWORD = os.environ.get("PASSWORD")
INVALID_USERNAME = "User"
INVALID_PASSWORD = "User123"
PAGE_TITLE = "GitHub"
ERROR_MSG = "Incorrect username or password."
