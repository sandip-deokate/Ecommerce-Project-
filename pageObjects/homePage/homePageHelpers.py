import time

from pageObjects.homePage.homePageElements import HomePageElements
from utilities.webDriverCommonMethods import webDriverCommonMethods
from utilities.webDriverCommonMethods import webDriverCommonMethods
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class homePageHelpers:
    def __init__(self,driver):
        self.driver=driver
        self.elements = HomePageElements(driver) # Instantiate the HomePageElements class
        self.webdrivermethods = webDriverCommonMethods(driver)
        self.act = ActionChains(self.driver)

    def click_my_account_dropdown(self):
        # Perform an action on the "My Account" dropdown
        dropdown = self.elements.get_my_account_link()
        self.act.move_to_element(dropdown).click(dropdown).perform()

    def click_login_link(self):
        # Perform an action on the "Register" link
        login_link = self.elements.get_login_link()
        login_link.click()

    def my_account_mouse_hover(self):

        my_account_link=self.elements.get_hello_str()
        try:
            self.act.move_to_element(my_account_link).perform()
        except:
            self.act.click(my_account_link).perform()
        finally:
            my_account_link.click()

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

    def click_log_out(self):
        time.sleep(2)
        dropdown = self.elements.get_my_account_link()
        self.act.move_to_element(dropdown).click(dropdown).perform()
        logout_link= self.elements.get_logout_link()
        self.act.move_to_element(logout_link).click(logout_link).perform()
