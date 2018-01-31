#coding=utf-8
import unittest
import sys
sys.path.append("..")
from public import BaseFunction,login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Test(unittest.TestCase):

    def setUp(self):
        self.dr=login.Login()
        self.driver=self.dr.getDriver()
        self.url=self.dr.getUrl()
        self.dr.login(self.dr.getDriver(),self.url)


    def tearDown(self):

        self.driver.quit()

    def test_all_skulist(self):
        self.driver.implicitly_wait(30)
        
        BaseFunction.getLocator(self.driver, "page_button").click()
        
        


if __name__ == "__main__":
    unittest.main()