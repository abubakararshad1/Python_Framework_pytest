import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Recruitment_Admin_Page:

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
