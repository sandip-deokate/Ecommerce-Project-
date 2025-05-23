import time

from pageObjects.homePage.homePageElements import HomePageElements
from utilities.webDriverCommonMethods import webDriverCommonMethods
from utilities.webDriverCommonMethods import webDriverCommonMethods
from selenium.common.exceptions import ElementClickInterceptedException
class homePageHelpers:
    def __init__(self,driver):
        self.driver=driver
        self.elements = HomePageElements(driver) # Instantiate the HomePageElements class
        self.webdrivermethods = webDriverCommonMethods(driver)

    """def click_my_account_dropdown(self):
        # Perform an action on the "My Account" dropdown
        dropdown = self.elements.get_my_account_dropdown()
        dropdown.click()"""

    def click_login_link(self):
        # Perform an action on the "Register" link
        login_link = self.elements.get_login_link()
        login_link.click()

    def get_hello_str(self):
        hello_str=self.elements.get_hello_str()
        return hello_str.text

    def click_bom_tool_link(self):
        bom_tool_link =self.elements.get_header_bom_tool_link()
        #self.web_method.wait_till_element_clickable(bom_tool_link)
        bom_tool_link.click()

    def click_accept_term_button(self):
        accept_term=self.webdrivermethods.wait_till_element_clickable(self.elements.get_accept_term_button())
        #accept_term=self.elements.get_accept_term_button()
        try:
            accept_term.click()
        except ElementClickInterceptedException:
            print("Element click intercepted. Trying JavaScript click.")
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", accept_term)
            time.sleep(2)
