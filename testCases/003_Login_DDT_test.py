import os
import time
import pytest
from utilities.customLogger import LogGen
from pageObjects.homePage.homePageHelpers import homePageHelpers
from pageObjects.loginPage.loginPageHelpers import loginPageHelpers
from utilities.readProperties import ReadConfig


class Test_003_Login_DDT():
    def test_003_login_DDT(self,browser_setup):
        driver= browser_setup
        baseUrl= ReadConfig.get_url()
        driver.get(baseUrl)

        home_page = homePageHelpers(driver)
        login_page = loginPageHelpers(driver)

        home_page.click_accept_term_button()
        home_page.click_login_link()

        login_page.submit_login_using_excel()












