from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.base_page import BasePage
import test_data as td


class MainPage(BasePage):
    def click_sign_in_btn(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(td.SIGN_IN_BTN)).click()
