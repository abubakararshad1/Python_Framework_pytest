from selenium import webdriver
import time

from base_pages.Admin_Sidebar import Admin_Sidebar
from base_pages.Login_Admin_Page import Login_Admin_Page
from test_cases.TC1_admin_login import Test_01_Admin_login


class Test_02_Admin_user_management:
    def __init__(self, driver):
     self.driver = driver

    admin_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


    empname ="a"
    username = "bsstest101"
    password = "bss123456"
    confirmpassword ="bss123456"

    def User_Login_Verification(self):
     #self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.login_admin = Login_Admin_Page(self.driver)
        self.login_admin.enter_username(self.username)
        self.login_admin.enter_password(self.password)
        self.login_admin.click_login()

    def create_user(self):
        # self.driver = webdriver.Chrome()
        self.saveuser = Admin_Sidebar(self.driver)
        self.saveuser.click_admin()
        self.saveuser.click_add_btn()
        time.sleep(5)
        self.saveuser.select_user_role()
        self.saveuser.enter_empname(self.empname)
        self.saveuser.select_Status()
        self.saveuser.enter_username(self.username)
        self.saveuser.enter_password(self.password)
        self.saveuser.enter_confirm_password(self.confirmpassword)
        self.saveuser.save_btn()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    # Step 2: Create an object of Login_Admin_Page class and pass the driver to it

    login_page = Test_01_Admin_login(driver)
    login_page.User_Login_Verification()


    add_user = Test_02_Admin_user_management(driver)
    add_user.create_user()


    time.sleep(50)
    driver.quit()
    # Step 3: Call the methods in the class to perform the login actions
