import pytest
import self as self
from selenium import webdriver
from PageObjects.LoginPage import Homepage
from TestCase.conftest import setup

class test_001_Login:
    BaseUrl="https://www.ebay.com/"

    def __init__(self):
        self.Homepage = None

    def test_ApplyingFilter(self,setup):
        self.driver=setup
        self.driver.get(self.BaseUrl)
        self.Homepage=Homepage.AllCategory()



