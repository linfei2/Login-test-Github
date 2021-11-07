from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.base_page import BasePage


class LoginPage(BasePage):

    username_field = (By.ID, "login_field")
    password_field = (By.ID, "password")
    submit_btn = (By.NAME, "commit")
    error_box = (By.XPATH, "//div[@class='container-lg px-2']")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_field))\
            .send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(self.password_field).send_keys(password)

    def submit(self):
        self.driver.find_element(self.submit_btn).click()

    def verify_error_msg(self, error_msg):
        msg = self.driver.find_element(self.error_box).get_attribute("innerText")
        assert msg == error_msg




