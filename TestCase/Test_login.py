from selenium import webdriver
from PageObjects.LoginPage import login
from TestCase.conftest import setup

class test_001_login_page():
    BaseUrl="https://www.ebay.com/"
    Username="skpraveen154@gmail.com"
    Password="Praveen@154"

    def HomePageTitle(self,setup):
        self.driver=webdriver.chrome()
        self.driver.get(self.BaseUrl)
        act_title=self.driver.title
        self.driver.close()
