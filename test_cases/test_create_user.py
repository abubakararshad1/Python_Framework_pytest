import allure
import time

import pytest

from base_pages.Admin_Create_User_Page import Admin_Create_User
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config


class Test_02_Admin_Create_User:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_password = Read_Config.get_invalid_password()

    empname1 = "a"
    username1 = "bsstest101"
    password1 = "bss1234567"
    confirmpassword1= "bss1234567"

    @allure.story('test_create_user')
    @pytest.mark.regression
    def test_create_user(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.login_admin = Login_Admin_Page(self.driver)
        self.login_admin.enter_username(self.username)
        self.login_admin.enter_password(self.password)
        self.login_admin.click_login()
        self.driver.implicitly_wait(5)

        # Adding System user


        self.create_user = Admin_Create_User(self.driver)
        self.create_user.click_admin()
        self.create_user.click_add_btn()
        time.sleep(5)
        self.create_user.select_user_role()
        self.create_user.enter_empname(self.empname1)
        self.create_user.select_Status()
        self.create_user.enter_username(self.username1)
        self.create_user.enter_password(self.password1)
        self.create_user.enter_confirm_password(self.confirmpassword1)
        self.create_user.save_btn()
        time.sleep(20)
