import time
from PageObjects.UserLoginPage import UserLogiPage
from Utilities.ReadCongi import Readconfig

class Test_loginpage:
    Username = Readconfig.getUsername()
    Password = Readconfig.getUsername()
    def Test_login_001(self, setup):
        self.driver = setup
        self.LP = UserLogiPage(self.driver)

        # 1. log in ebay account
        self.LP.Click_LoginButton()
        # self.driver.find_element(By.XPATH, '//*[@id="gh-ug"]/a').click()

        time.sleep(10)

        # 2. click on the checkbox
        # browser.find_element(By.ID,"checkbox").click()

        # 3. Enter the username
        self.LP.Enter_Username("skpraveen154@gmail.com")
        # self.driver.find_element(By.ID, "userid").send_keys("skpraveen154@gmail.com")

        # 4. click the continue button
        self.LP.Click_ContinueButton()
        # self.driver.find_element(By.ID, "signin-continue-btn").click()

        # 5. enter the password
        self.LP.Enter_Password("Praveen@154")
        # self.driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('Praveen@154')

        # 6. Click on password sign in button
        self.LP.Click_SignButton()
        # self.driver.find_element(By.ID, "sgnBt").click()

        # 7. checking page validation
        if self.LP.Status() == True:
            self.driver.save_screenshot("E:\\pythonProject\\ebayCommerceApp\\Screenshots\\Test_loginpage_001_pass.png")
            assert True
        else:
            self.driver.save_screenshot("E:\\pythonProject\\ebayCommerceApp\\Screenshots\\Test_loginpage_001_fail.png")
            assert False
