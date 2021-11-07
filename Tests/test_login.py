import os
import unittest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_valid_login(self):
        mp = MainPage(self.driver)
        mp.click_sign_in_btn()
        lp = LoginPage(self.driver)
        username = os.environ.get("LOGIN")
        password = os.environ.get("PASSWORD")
        lp.enter_username(username)
        lp.enter_password(password)
        lp.submit()
        assert "GitHub" in self.driver.title


if __name__ == "__main__":
    unittest.main()
