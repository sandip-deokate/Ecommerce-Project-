from idna import check_hyphen_ok

from selenium.webdriver.common.by import By

class registerPageElements():
    def __init__(self,driver):
        self.driver = driver

    # Define Elements
    txt_firstName = (By.XPATH, "//input[@id='input-firstname']")
    txt_lastName = (By.XPATH, "//input[@id='input-lastname']")
    txt_email = (By.XPATH, "//input[@id='input-email']")
    #txt_password = (By.XPATH, "//input[@id='input-password']")
    chk_privacyPolicy = (By.XPATH, "input[@name='agree']")
    btn_Submit = (By.XPATH, "//button[@type='submit']")
    str_AccountHasBeenCreated = (By.XPATH, "//div[@id='content']/h1")

    txt_username = (By.XPATH,"//input[@id='username']")
    txt_password = (By.XPATH,"//input[@id='password']")
    btn_login = (By.XPATH,"//div[@class='u-align-right']/button")

    def get_txt_firstName(self):
        return self.driver.find_element(*self.txt_firstName)

    def get_txt_lastName(self):
        return self.driver.find_element(*self.txt_lastName)

    def get_txt_email(self):
        return self.driver.find_element(*self.txt_email)

    def get_txt_password(self):
        return self.driver.find_element(*self.txt_password)

    def get_chk_privacyPolicy(self):
        return self.driver.find_element(*self.chk_privacyPolicy)

    def get_btn_Submit(self):
        return self.driver.find_element(*self.btn_Submit)

    def get_str_AccountHasBeenCreated(self):
        return  self.driver.find_element(*self.str_AccountHasBeenCreated)

    def get_username(self):
        return self.driver.find_element(*self.txt_username)

    def get_btn_login(self):
        return self.driver.find_element(*self.btn_login)
