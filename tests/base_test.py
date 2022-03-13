import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import test_data as td


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(td.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
