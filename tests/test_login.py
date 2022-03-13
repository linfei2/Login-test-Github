import unittest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests.base_test import BaseTest
import test_data as td


class TestLogin(BaseTest):
    def test_valid_login(self):
        mp = MainPage(self.driver)
        mp.click_sign_in_btn()
        lp = LoginPage(self.driver)
        lp.enter_username(td.VALID_USERNAME)
        lp.enter_password(td.VALID_PASSWORD)
        lp.submit()
        lp.verify_page_title(td.PAGE_TITLE)

    def test_invalid_login(self):
        mp = MainPage(self.driver)
        mp.click_sign_in_btn()
        lp = LoginPage(self.driver)
        lp.enter_username(td.INVALID_USERNAME)
        lp.enter_password(td.INVALID_PASSWORD)
        lp.submit()
        lp.verify_error_msg(td.ERROR_MSG)


if __name__ == "__main__":
    unittest.main()
