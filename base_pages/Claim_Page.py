import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Claim_Page:

    sidepanel_claim_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span"
    btn_assign_claim_xpath = "(//button[contains(@class,'oxd-button oxd-button--medium oxd-button--secondary')])[2]"
    textbox_employee_name_xpath = "//input[@placeholder='Type for hints...']"
    dropdown_click_event_xpath = "(//div[contains(.,'-- Select --')])[14]"
    dropdown_select_event_xpath = "(//div[contains(.,'Travel Allowance')])[13]/div[2]/span[1]"
    dropdown_click_currency_xpath = "(//div[contains(@class,'oxd-select-text-input')])[2]"
    dropdown_select_currency_xpath = "//span[contains(.,'Afghanistan Afghani')]"
    textbox_remarks_xpath = "//textarea[contains(@class,'oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical')]"
    btn_create_xpath = "//button[@type='submit']"




    # driver = webdriver.Chrome()
    def __init__(self, driver):
        self.driver = driver
    # Path - Click left admin panel

    # Path - click add button

    def side_panel_click_clm_btn(self):
        # Wait for the username field to be visible before interacting
        clm_btn = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.sidepanel_claim_xpath))
        )
        clm_btn.click()
        time.sleep(5)

    def click_assign_clm_btn(self):
        # Wait for the username field to be visible before interacting
        assign_clm_btn = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_assign_claim_xpath))
        )
        assign_clm_btn.click()
        time.sleep(5)

    def enter_employee_name(self, employee_name):
        # Wait for the username field to be visible before interacting
        emp_name = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_employee_name_xpath))
        )

        emp_name.send_keys(employee_name)
        time.sleep(5)
        select_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='listbox']/div[@role='option'][1]"))
        )
        select_option.click()


    def select_event_role(self):


        click_event = WebDriverWait(self.driver, 20).until(
             EC.visibility_of_element_located((By.XPATH, self.dropdown_click_event_xpath)))
        time.sleep(5)
        click_event.click()

        select_event = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.dropdown_select_event_xpath)))
        select_event.click()

    def select_currency (self):
        # Wait for the password field to be visible before interacting
        click_currency = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.dropdown_click_currency_xpath))
        )
        click_currency.send_keys("af")
        time.sleep(5)
        select_currency  = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='option'][2]"))
        )
        select_currency.click()


    def enter_remarks(self, remarks):
        # Wait for the password field to be visible before interacting
        remarks_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_remarks_xpath))
        )
        remarks_field.clear()
        remarks_field.send_keys(remarks)

    def click_create(self):
        # Wait for the password field to be visible before interacting
        create_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_create_xpath))
        )

        create_btn.click()


    # --------------------------  Assign claims to the user  --------------------------------

    btn_add_expense_xpath = "(//button[@type='button' and @class='oxd-button oxd-button--medium oxd-button--text'])[1]"
    dropdown_click_Expense_type_xpath = "//div[@class='oxd-select-text-input']"
    dropdown_select_Expense_type_xpath = "//span[contains(.,'Transport')]"
    textbox_enter_amount_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[6]/div/div/div/form/div[2]/div/div[2]/div/div[2]/input"
    textbox_enter_date_xpath = "//input[@placeholder='yyyy-dd-mm']"
    textbox_enter_notes_xpath = "(//*[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[2]"
    btn_save_xpath = "//button[@type='submit']"

    def click_add_expense_btn(self):
        # Wait for the username field to be visible before interacting
        clm_btn = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_add_expense_xpath))
        )
        clm_btn.click()


    def select_expense_type(self):
        click_currency = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.dropdown_click_Expense_type_xpath))
        )
        click_currency.click()
        time.sleep(3)
        select_currency = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.dropdown_select_Expense_type_xpath))
        )
        select_currency.click()
    def enter_date(self, date):
        # Wait for the password field to be visible before interacting
        date_enter = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_enter_date_xpath))
        )
        date_enter.clear()
        date_enter.send_keys(date)


    def enter_amount(self, amount):
        # Wait for the password field to be visible before interacting
        enter_amounts = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_enter_amount_xpath))
        )
        enter_amounts.clear()
        enter_amounts.send_keys(amount)

    def enter_notes(self, notes):
        # Wait for the password field to be visible before interacting
        remarks_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_enter_notes_xpath))
        )
        remarks_field.clear()
        remarks_field.send_keys(notes)

    def click_save_btn(self):
        # Wait for the password field to be visible before interacting
        remarks_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_save_xpath))
        )
        remarks_field.click()
