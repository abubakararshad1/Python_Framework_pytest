from selenium import webdriver
import time
from base_pages.Login_Admin_Page import Login_Admin_Page


class Test_01_Admin_login:
    def __init__(self, driver):
     self.driver = driver

    admin_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    username = "Admin"
    password = "admin123"

    def User_Login_Verification(self):
     #self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.login_admin = Login_Admin_Page(self.driver)
        self.login_admin.enter_username(self.username)
        self.login_admin.enter_password(self.password)
        self.login_admin.click_login()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    # Step 2: Create an object of Login_Admin_Page class and pass the driver to it
    login_page = Test_01_Admin_login(driver)
    login_page.User_Login_Verification()
    time.sleep(5)
    driver.quit()
    # Step 3: Call the methods in the class to perform the login actions
