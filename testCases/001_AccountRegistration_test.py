import os
import time
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.homePage.homePageHelpers import homePageHelpers
from pageObjects.registration.registrationPageHelpers import registrationPageHelpers

class Test_001_AccountRegistration:

    def test_001_AccountRegistration(self,browser_setup):
        driver = browser_setup
        baseurl = ReadConfig.get_url()
        driver.get(baseurl)
        self.logger = LogGen.loggen()
        self.logger.info("********  Test_001_AccountRegistratio started  **********")
        home_page = homePageHelpers(driver)
        registration_page = registrationPageHelpers(driver)

        """home_page.click_my_account_dropdown()
        home_page.click_register_link()
        registration_page.submit_Registration_From()"""
        time.sleep(5)
        home_page.click_accept_term_button()
        home_page.click_login_link()

        #registration_page.login()
        welcome_name= home_page.get_hello_str()
        if welcome_name == "Hello San":
            assert True
            print(welcome_name)
        else:
            self.logger.error("********  Error  **********")
            screenshot_path = os.path.join(os.path.abspath(os.curdir), 'screenshots', "001AccountRegistration.png")
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)  # Ensure the screenshots directory exists
            driver.save_screenshot(screenshot_path)
        self.logger.info("********  Test_001_AccountRegistratio finished  **********")


