from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.base_page import BasePage
import test_data as td


class LoginPage(BasePage):
    def enter_username(self, username):
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(td.USERNAME_FIELD)) \
            .send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*td.PASSWORD_FIELD).send_keys(password)

    def submit(self):
        self.driver.find_element(*td.SUBMIT_BTN).click()

    def verify_page_title(self, title):
        assert title == self.driver.title

    def verify_error_msg(self, error_msg):
        msg = WebDriverWait(self.driver, 10).\
            until(lambda s: s.find_element(*td.ERROR_BOX)).get_attribute("innerText")
        assert msg == error_msg
