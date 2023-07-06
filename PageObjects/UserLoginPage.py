from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Utilities.ReadCongi import Readconfig


class UserLogiPage:
    Username = Readconfig.getUsername()
    Password = Readconfig.getUsername()

    Click_LoginButton_XPATH = (By.XPATH, '//*[@id="gh-ug"]/a')
    Enter_Username_ID = (By.ID, "userid")
    Click_ContinueButton_ID = (By.ID, "signin-continue-btn")
    Enter_Password_XPATH = (By.XPATH, '//*[@id="pass"]')
    Click_SignButton_ID = (By.ID, "sgnBt")
    Status_Title = "Electronics, Cars, Fashion, Collectibles & More | eBay"

    def __init__(self, driver):
        self.driver = driver

    def Click_LoginButton(self):
        self.driver.find_element(*UserLogiPage.Click_LoginButton_XPATH).click()

    def Enter_Username(self):
        self.driver.find_element(*UserLogiPage.Enter_Username_ID).send_keys(self.Username)

    def Click_ContinueButton(self):
        self.driver.find_element(*UserLogiPage.Click_ContinueButton_ID).click()

    def Enter_Password(self):
        self.driver.find_element(*UserLogiPage.Enter_Password_XPATH).send_keys(self.Password)

    def Click_SignButton(self):
        self.driver.find_element(*UserLogiPage.Click_SignButton_ID).click()

    def Status(self):
        try:
            self.driver.title(*UserLogiPage.Status_Title)
            return True
        except NoSuchElementException:
            return False
