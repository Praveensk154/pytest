class Test_login:
    textbox_username_id = "userid"
    login_button_continue_xpath = "//*[@id='signin-continue-btn']"
    Textbox_password_id = "pass"
    login_button_signin_xpath = "//*[@id=['sgnBt']"
    Sign_out_xpath = "//*[@id='gh-uo']/a"

    def __int__(self, driver):
        self.driver = driver

    def setpassword(self):
        self.driver.find_element_by_id(self.Textbox_password_id).clear()
        self.driver.find_element_by_id(self.Textbox_password_id).send_keys("password")

    def clicksignout(self):
        self.driver.find_element_by_xpath(self.Sign_out_xpath).click()

