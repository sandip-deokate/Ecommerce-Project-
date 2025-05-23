from selenium.webdriver.common.by import By
class BomToolPageElements:
    def __init__(self,driver):
        self.driver=driver
        self.bom_tool_page_title=(By.XPATH,"//h1[normalize-space()='BOM Management']")

        self.upload_bom =(By.XPATH,"//input[@type='file']")

    def get_bom_tool_page_elements(self):
        return self.driver.find_element(*self.bom_tool_page_title)

    def get_upload_bom(self):
        return self.driver.find_element(*self.upload_bom)