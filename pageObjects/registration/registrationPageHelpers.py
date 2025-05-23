import os.path
import openpyxl
from utilities.excel_Operations import ExcelOperations
from pageObjects.registration.registerPageElements import registerPageElements
from utilities.randomDataGenerator import ramdom_Email_Generator
from utilities.readProperties import ReadConfig
from utilities.webDriverCommonMethods import webDriverCommonMethods

class registrationPageHelpers:
    def __init__(self,driver):
        self.elements = registerPageElements(driver)
        self.webdrivermethods=webDriverCommonMethods(driver)
        self.excelOperations= ExcelOperations(driver)
    """def submit_Registration_From(self):
        firstName=self.elements.get_txt_firstName()
        firstName.send_keys("S")

        lastName=self.elements.get_txt_lastName()
        lastName.send_keys("D")"""

    """def submit_login_using_conf(self):
        username = self.elements.get_username()
        email=ReadConfig.get_email()
        username.send_keys(email)
        password = ReadConfig.get_password()
        passowrd= self.elements.get_txt_password()
        passowrd.send_keys(password)
        #self.webdrivermethods.scroll_till_element_located(self.elements.get_btn_login())
        btn_login = self.elements.get_btn_login()
        btn_login.click()"""

    def submit_login_using_excel(self):
        path = os.path.abspath((os.curdir)+'//testData//'+ 'BomShort.xlsx')
        sheet='Login Data'
        max_row=self.excelOperations.get_max_row(path,sheet)
        max_col=self.excelOperations.get_max_col(path,sheet)

        











