import allure
import time

import pytest

from base_pages.Claim_Page import Claim_Page
from base_pages.Login_Admin_Page import Login_Admin_Page
from test_cases.test_recruitment_admin import Test_03_Admin_Add_candidate
from utilities.read_properties import Read_Config

class Test_04_Admin_Create_Claim:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    employee_name = "th"
    remarks = "This is testing"


    date = "2025-06-03"
    amount = "2000"
    note = "This is my ab testing"

    @allure.story('test_create_claim')
    @pytest.mark.regression
    def test_create_claim(self, setup):
        test1 = Test_03_Admin_Add_candidate()
        note1 = test1.notes
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.login_admin = Login_Admin_Page(self.driver)
        self.login_admin.enter_username(self.username)
        self.login_admin.enter_password(self.password)
        self.login_admin.click_login()
        self.driver.implicitly_wait(5)
        self.create_claim = Claim_Page(self.driver)
        self.create_claim.side_panel_click_clm_btn()
        self.create_claim.click_assign_clm_btn()
        self.create_claim.enter_employee_name(self.employee_name)
        self.create_claim.select_event_role()
        self.create_claim.select_currency()
        self.create_claim.enter_remarks(note1)
        self.create_claim.click_create()
        time.sleep(20)
        self.create_claim.click_add_expense_btn()
        self.create_claim.select_expense_type()
        self.create_claim.enter_date(self.date)
        self.create_claim.enter_amount(self.amount)
        self.create_claim.enter_notes(note1)
        self.create_claim.click_save_btn()

        time.sleep(15)





