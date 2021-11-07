from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.base_page import BasePage


class MainPage(BasePage):

    sign_in_btn = (By.XPATH, "//a[@href='/login']")

    def click_sign_in_btn(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.sign_in_btn)).click()
