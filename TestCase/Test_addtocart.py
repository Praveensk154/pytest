import time
from selenium.webdriver.common.by import By

class Test_addtocart:

    def Test_addtocart_001(self, setup):
        self.driver = setup

        # 8. searching for catergory

        self.driver.find_element(By.ID, "gh-cat").click()

        time.sleep(3)
        # 9. select the item in the dropdown
        item = self.driver.find_element(By.XPATH, "/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[2]/div/select/option[8]")
        item.click()

        # 10. click on search
        self.driver.find_element(By.ID, "gh-btn").click()
        # page title : Electronics, Cars, Fashion, Collectibles & More | eBay

        # 11. searching item in webpage and select
        self.driver.find_element(By.CLASS_NAME, "b-visualnav__title").click()

        time.sleep(3)
        # 12. click on iphone 11
        self.driver.find_element(By.CLASS_NAME, "b-guidancecard__title").click()

        # 13. add to cart process
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div[3]/div[1]/section[1]/div[2]/div/div/ul/li[1]/a/p").click()

        # 14. switch to diffrent window
        self.driver.find_element(By.CLASS_NAME, "s-item__title").click()

        # 15. switch to new window to add item in add cart
        all_handles = self.driver.window_handles
        print(f"window_handle_before : ", all_handles)
        self.driver.switch_to.window(all_handles[-1])
        print(f"page handles : ", all_handles[-1])
        Page_title = self.driver.title
        print(f"Page_title : ", Page_title)

        # 17. select to add cart
        add_cart = self.driver.find_element(By.CLASS_NAME, "ux-call-to-action__text")
        add_cart.click()
