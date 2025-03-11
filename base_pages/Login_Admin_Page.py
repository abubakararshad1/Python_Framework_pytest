import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Admin_Page:
    textbox_username_name = "username"
    textbox_password_name = "password"
    btn_login_xpath = "//button[@type='submit']"
    #admin_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # Provided Data
    # username = "Admin"
    # password = "admin123"

    # driver = webdriver.Chrome()
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        # Wait for the username field to be visible before interacting
        username_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, self.textbox_username_name))
        )
        # time.sleep(5)
        # username_field = driver.find_element(By.NAME, self.textbox_username_name)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        # Wait for the password field to be visible before interacting
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.textbox_password_name))
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        # Wait for the login button to be clickable before clicking
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_login_xpath))
        )
        login_button.click()

