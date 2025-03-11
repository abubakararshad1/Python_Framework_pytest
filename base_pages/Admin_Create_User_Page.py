import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Admin_Create_User:
    textbox_username_name = "username"
    textbox_password_name = "password"
    btn_login_xpath = "//button[@type='submit']"
    admin_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    sidepanel_admin_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"
    btn_add_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
    dropdown_userrole_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[1]/div[1]"
    select_dropdown_userrole_xpath = "//div[@role='option'][2]"
    textbox_empname_xpath = "//input[@placeholder='Type for hints...']"
    dropdown_status_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div"
    textbox_username_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input"
    textbox_password_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]"
    text_confirmpassword_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]"
    btn_save_xpath = "//button[@type='submit']"



    # driver = webdriver.Chrome()
    def __init__(self, driver):
        self.driver = driver
    # Path - Click left admin panel

    # Path - click add button
    def click_admin(self):
        # Wait for the username field to be visible before interacting
        admin_side = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.sidepanel_admin_xpath))
        )
        admin_side.click()

    def click_add_btn(self):
        # Wait for the username field to be visible before interacting
        add_btn = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_add_xpath))
        )
        add_btn.click()
        time.sleep(5)


    def select_user_role(self):


        user_role_field = WebDriverWait(self.driver, 20).until(
             EC.visibility_of_element_located((By.XPATH, self.dropdown_userrole_xpath)))
        time.sleep(5)
        user_role_field.click()

        select_role_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.select_dropdown_userrole_xpath))
        )
        time.sleep(5)
        select_role_field.click()

    def enter_empname(self, empname):
        # Wait for the password field to be visible before interacting
        empname_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_empname_xpath))
        )
        empname_field.send_keys("a")
        time.sleep(5)
        select_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='option'][1]"))
        )

        select_option.click()



    def select_Status (self):
        # Wait for the login button to be clickable before clicking
        click_status = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.dropdown_status_xpath))
        )
        click_status.click()

        select_status_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='option'][2]"))
        )
        select_status_dropdown.click()


    def enter_username(self, username):
        # Wait for the password field to be visible before interacting
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath))
        )

        username_field.send_keys(username)

    def enter_password(self, password):
        # Wait for the password field to be visible before interacting
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_password_xpath))
        )
        password_field.clear()
        password_field.send_keys(password)

    def enter_confirm_password(self, confirmpassword):
        # Wait for the password field to be visible before interacting
        confirm_password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.text_confirmpassword_xpath))
        )
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirmpassword)

    def save_btn(self):
        # Wait for the password field to be visible before interacting
        save_btn_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_save_xpath))
        )
        save_btn_field.click()
