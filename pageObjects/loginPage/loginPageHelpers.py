import os.path
from fileinput import close

import openpyxl

from utilities.excel_Operations import ExcelOperations
from pageObjects.loginPage.loginPageElements import loginPageElements
from utilities.randomDataGenerator import ramdom_Email_Generator
from utilities.readProperties import ReadConfig
from utilities.webDriverCommonMethods import webDriverCommonMethods
from pageObjects.homePage.homePageHelpers import homePageHelpers
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class loginPageHelpers:
    def __init__(self, driver):
        self.driver=driver
        self.elements = loginPageElements(driver)
        self.webdrivermethods = webDriverCommonMethods(driver)
        self.excelOperations = ExcelOperations(driver)
        self.home_page = homePageHelpers(driver)


    def submit_login_using_conf(self):
        username = self.elements.get_username()
        email = ReadConfig.get_email()
        username.send_keys(email)
        password = ReadConfig.get_password()
        passowrd = self.elements.get_txt_password()
        passowrd.send_keys(password)
        # self.webdrivermethods.scroll_till_element_located(self.elements.get_btn_login())
        btn_login = self.elements.get_btn_login()
        btn_login.click()


    def submit_login_using_excel(self):

        path = os.path.join(os.path.abspath(os.curdir), 'testData', 'Login_DDT.xlsx')
        sheet = 'Sheet1'
        max_row = self.excelOperations.get_max_row(path, sheet)
        max_col = self.excelOperations.get_max_col(path, sheet)

        headerRowCountFile=1
        i=headerRowCountFile+1
        for i in range(i,max_row+1):
            email=self.excelOperations.read_data(path,sheet,i,1)
            passw=self.excelOperations.read_data(path,sheet,i,2)
            username = self.elements.get_username()
            username.clear()
            username.send_keys(email)
            password=self.elements.get_txt_password()
            password.clear()
            password.send_keys(passw)
            btn_login = self.elements.get_btn_login()
            btn_login.click()
            try:
                time.sleep(10)
                welcome_name = self.home_page.get_hello_str()
                if welcome_name == "Hello San":
                    value = self.excelOperations.write_Data(path, sheet, i, 4, "PASS")
                    self.home_page.click_log_out()
                    time.sleep(2)
                    self.home_page.click_login_link()
                else:
                    self.excelOperations.write_Data(path, sheet, i, 4, "FAIL")
            except NoSuchElementException as e:
                print(f"An error occurred: {e}")
                time.sleep(2)

