import time
import allure
import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
class Test_01_Admin_login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_password = Read_Config.get_invalid_password()

    @allure.story('test_Valid_Login_Verification')
    def test_Valid_Login_Verification(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.login_admin = Login_Admin_Page(self.driver)
        self.login_admin.enter_username(self.username)
        self.login_admin.enter_password(self.password)
        self.login_admin.click_login()
        self.driver.implicitly_wait(5)
        act_dashboard_text = self.driver.find_element(By.XPATH,"//h6[contains(.,'Dashboard')]").text
        if act_dashboard_text == "Dashboard":
            assert True
            self.driver.close()
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\screenshots\\test_Valid_Login_Verification.png")
            # self.driver.get_screenshot_as_file("./screenshots/test_User_Valid_Login_Verification.png")
            self.driver.close()
            assert False


    def test_Invalid_Login_Verification(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.login_admin = Login_Admin_Page(self.driver)
        self.login_admin.enter_username(self.username)
        self.login_admin.enter_password(self.invalid_password)
        self.login_admin.click_login()
        self.driver.implicitly_wait(5)
        act_dashboard_text = self.driver.find_element(By.XPATH,"//p[contains(.,'Invalid credentials')]").text
        if act_dashboard_text == "Invalid credentials":
            assert True
            self.driver.close()
        else:
            time.sleep(5)
            self.driver.save_screenshot(".\\screenshots\\test_Invalid_Login_Verification.png")
            self.driver.close()
            assert False


