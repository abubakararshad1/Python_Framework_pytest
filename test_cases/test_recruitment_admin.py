import time
import allure
import pytest

from base_pages.Recruitment_Admin_Page import Recruitment_Admin_Page
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
class Test_03_Admin_Add_candidate:

    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()

    first_name = "mian"
    middle_name = "abubakar"
    last_name = "arshad"
    email = "abubakar.arshad1@gmail.com"
    contact_no = "0323-4010253"
    keywords = "abx,xyz"
    date_of_application = "2025-25-02"
    notes = "1000 ka note"

    @allure.story('create recruitment')
    @pytest.mark.regression
    def test_create_recruitment(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.login_admin = Login_Admin_Page(self.driver)
        self.login_admin.enter_username(self.username)
        self.login_admin.enter_password(self.password)
        self.login_admin.click_login()
        self.driver.implicitly_wait(5)

        #add candidate information

        self.recruitment_page = Recruitment_Admin_Page(self.driver)
        self.recruitment_page.click_recruitment()
        self.recruitment_page.add_btn()
        self.recruitment_page.enter_firstname(self.first_name)
        self.recruitment_page.enter_middlename(self.middle_name)
        self.recruitment_page.enter_lastname(self.last_name)
        self.recruitment_page.enter_email(self.email)
        self.recruitment_page.click_vacancy()
        self.recruitment_page.select_vacancy()
        self.recruitment_page.enter_contactno(self.contact_no)
        self.recruitment_page.enter_keyword(self.keywords)
        self.recruitment_page.enter_notes(self.notes)
        self.recruitment_page.save_btn()
        time.sleep(5)







