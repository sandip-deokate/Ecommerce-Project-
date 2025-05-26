from selenium.webdriver.common.by import By

class loginPageElements():
    def __init__(self,driver):
        self.driver = driver

    txt_username = (By.XPATH,"//input[@id='username']")
    txt_password = (By.XPATH,"//input[@id='password']")
    btn_login = (By.XPATH,"//div[@class='u-align-right']/button")

    def get_username(self):
        return self.driver.find_element(*self.txt_username)

    def get_txt_password(self):
        return self.driver.find_element(*self.txt_password)

    def get_btn_login(self):
        return self.driver.find_element(*self.btn_login)
