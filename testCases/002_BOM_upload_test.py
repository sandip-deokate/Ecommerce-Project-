import os
import time
import pytest
from utilities.readProperties import ReadConfig
from pageObjects.homePage.homePageHelpers import homePageHelpers
from pageObjects.BomToolPage.bomToolPageHelpers import bomToolPageHelpers
from pageObjects.registration.registrationPageHelpers import registrationPageHelpers

class Test_BOM_Upload:

    def test_002_bom_upload(self,browser_setup):
        driver=browser_setup
        baseurl = ReadConfig.get_url()
        driver.get(baseurl)
        driver.implicitly_wait(20)
        home_page= homePageHelpers(driver)
        bom_page=bomToolPageHelpers(driver)
        registration_page = registrationPageHelpers(driver)


        home_page.click_accept_term_button()
        home_page.click_login_link()
        #registration_page.login()
        registration_page.submit_login_using_excel()
        time.sleep(20)
        home_page.click_bom_tool_link()
        bom_page_title=bom_page.get_bom_tool_page_title()

        bom_page.upload_bom_file()
        #assert bom_page_title=="BOM Management"


        time.sleep(10)



