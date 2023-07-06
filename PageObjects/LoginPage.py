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

class Homepage:
    All_category_xpath="//*[@id='gh-cat']"
    Cell_phones_value="15032"
    Search_option_class="btn btn-prim gh-spr"
    Cell_smartphone_class="b-visualnav__title"
    filter_button_type="button"
    SwitchFrame_class="x-overlay__container"


    def __int__(self,driver):
        self.driver=driver

    def AllCategory(self):
        self.driver.find_element_by_xpath(self.All_category_xpath).clear()
        self.driver.find_element_by_xpath(self.All_category_xpath).click()

    def Search_option(self):
        self.driver.find_element_by_class(self.Search_option_class).click()

    def Cell_phones(self):
        self.driver.find_element_by_class(self.Cell_smartphone_class).click()

    def Filter_button(self):
        self.driver.find_element_by_type(self.filter_button_type).click()

    def Switch_frame(self):
        self.driver.Switch_to.frame()

