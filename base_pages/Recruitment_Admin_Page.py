import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_cases.TC1_admin_login import Test_01_Admin_login


class Recruitment_Admin_Page:
    admin_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    textbox_first_name = "mian"
    textbox_middle_name = "abubakar"
    textbox_last_name = "arshad"
    dropdown_vacancy = "//button[@type='submit']"
    textbox_email = "abubakar.arshad1@gmail.com"
    textbox_contact_no = "0323-4010253"
    textbox_keywords = "abx,xyz"
    textbox_date_of_application = "2025-25-02"
    textbox_notes = "This is my testing and i am testing up the things"

    Recruitment_sidepanel_xpath = "//span[contains(.,'Recruitment')]"
    recruitment_add_btn_xpath = "//button[@type='button'][contains(.,'Add')]"
    textbox_first_name_xpath = "//input[@name='firstName']"
    textbox_middle_name_xpath = "//input[contains(@name,'middleName')]"
    textbox_last_name_xpath = "//input[contains(@name,'lastName')]"
    dropdown_vacancy_xpath = "//div[@class='oxd-select-text-input']" #(//div[@tabindex='0'])[2]/ancestor::div[1]//following-sibling::div[1]"
    dropdown_vacancy_select_xpath = "//*[@class='oxd-select-text oxd-select-text--focus']/following-sibling::div[1]/div[5]"

    textbox_email_xpath = "(//input[contains(@placeholder,'Type here')])[1]"
    textbox_contact_no_xpath = "(//input[contains(@placeholder,'Type here')])[2]"
    textbox_keywords_xpath = "//input[@placeholder='Enter comma seperated words...']"
    textbox_date_of_application_xpath = "//input[contains(@placeholder,'yyyy-dd-mm')]"
    textbox_notes_xpath = "//textarea[contains(@placeholder,'Type here')]"
    textbox_save_xpath = "//button[@type='submit']"
    # Provided Data
    # username = "Admin"
    # password = "admin123"

    # driver = webdriver.Chrome()
    def __init__(self, driver):
        self.driver = driver

    def click_recruitment(self):
        # Wait for the username field to be visible before interacting
        click_recruitment_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.Recruitment_sidepanel_xpath)))

        # time.sleep(5)
        # username_field = driver.find_element(By.NAME, self.textbox_username_name)
        click_recruitment_field.click()

    def add_btn(self):
        # Wait for the username field to be visible before interacting
        click_add_btn = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.recruitment_add_btn_xpath))
        )
        # time.sleep(5)
        # username_field = driver.find_element(By.NAME, self.textbox_username_name)
        click_add_btn.click()

    def enter_firstname(self, firstname):
        firstname_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_first_name_xpath))
        )
        firstname_field.clear()
        firstname_field.send_keys(firstname)

    def enter_middlename(self, middlename):
        middlename_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_middle_name_xpath))
        )
        middlename_field.clear()
        middlename_field.send_keys(middlename)

    def enter_lastname(self, lastname):
        # Wait for the login button to be clickable before clicking
        lastname_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textbox_last_name_xpath))
        )
        lastname_field.clear()
        lastname_field.send_keys(lastname)


    def click_vacancy(self):
        # Wait for the login button to be clickable before clicking
        click_vacancy_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.dropdown_vacancy_xpath))
        )
        # click_vacancy_field.clear()
        click_vacancy_field.click()

    def select_vacancy(self):
        # Wait for the login button to be clickable before clicking
        select_vacancy_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.dropdown_vacancy_select_xpath))
        )

        select_vacancy_field.click()

    def enter_email(self, email):
        # Wait for the login button to be clickable before clicking
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textbox_email_xpath))
        )
        email_field.clear()
        email_field.send_keys(email)

    def enter_contactno(self, contactno):
        # Wait for the login button to be clickable before clicking
        contactno_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textbox_contact_no_xpath))
        )
        contactno_field.clear()
        contactno_field.send_keys(contactno)

    def enter_keyword(self, keyword):
        # Wait for the login button to be clickable before clicking
        keyword_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textbox_keywords_xpath))
        )
        keyword_field.clear()
        keyword_field.send_keys(keyword)

    def enter_Doa(self, doa):
        # Wait for the login button to be clickable before clicking
        doa_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textbox_date_of_application_xpath))
        )
        doa_field.clear()
        time.sleep(5)
        doa_field.send_keys(doa)

    def enter_notes(self, notes):
        # Wait for the login button to be clickable before clicking
        notes_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textbox_notes_xpath))
        )
        notes_field.clear()
        notes_field.send_keys(notes)

    def save_btn(self):
        # Wait for the login button to be clickable before clicking
        notes_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.textbox_save_xpath))
        )

        notes_field.click()

    # def User_Login_Verification(self):
    #     self.driver.get(self.admin_page_url)
    #     self.enter_username(self.username)
    #     self.enter_password(self.password)
    #     self.click_login()





if __name__ == "__main__":
    # Step 1: Initialize the WebDriver (Assuming you're using Chrome here)
    PATH = '../driver/chromedriver.exe'
    driver = webdriver.Chrome()  # Make sure chromedriver is installed and accessible
    driver.get(Recruitment_Admin_Page.admin_page_url)
    login_page = Test_01_Admin_login(driver)
    login_page.User_Login_Verification()

    # Step 2: Create an object of Login_Admin_Page class and pass the driver to it
    Recruitment_page = Recruitment_Admin_Page(driver)
    time.sleep(5)
    Recruitment_page.click_recruitment()
    Recruitment_page.add_btn()
    time.sleep(5)
    Recruitment_page.enter_firstname(Recruitment_Admin_Page.textbox_first_name)
    time.sleep(2)
    Recruitment_page.enter_middlename(Recruitment_Admin_Page.textbox_middle_name)
    time.sleep(2)
    Recruitment_page.enter_lastname(Recruitment_Admin_Page.textbox_last_name)
    time.sleep(2)
    Recruitment_page.enter_email(Recruitment_Admin_Page.textbox_email)
    time.sleep(5)
    Recruitment_page.click_vacancy()
    time.sleep(5)
    Recruitment_page.select_vacancy()

    Recruitment_page.enter_contactno(Recruitment_Admin_Page.textbox_contact_no)
    time.sleep(5)
    Recruitment_page.enter_keyword(Recruitment_Admin_Page.textbox_keywords)
    time.sleep(5)
    # Recruitment_page.enter_Doa(Recruitment_Admin_Page.textbox_date_of_application)
    # time.sleep(5)
    Recruitment_page.enter_notes(Recruitment_Admin_Page.textbox_notes)
    time.sleep(5)
    Recruitment_page.save_btn()  # Save the form

    time.sleep(25)
    driver.quit()
    # Step 3: Call the methods in the class to perform the login actions


# if __name__ == "__main__":
#     # Step 1: Initialize the WebDriver (Assuming you're using Chrome here)
#     driver = webdriver.Chrome()  # Make sure chromedriver is installed and accessible
#
#     # Step 2: Create an object of Login_Admin_Page class and pass the driver to it
#     login_page = Login_Admin_Page(driver)
#     login_page.User_Login_Verification()
#     time.sleep(25)
#     driver.quit()
#     # Step 3: Call the methods in the class to perform the login actions
