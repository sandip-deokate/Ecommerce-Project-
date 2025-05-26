from selenium.webdriver.common.by import By
class HomePageElements:
    def __init__(self, driver):
        self.driver = driver
    # Define the elements

    #my_account_dropdown = (By.XPATH, "//span[text()='My Account']")

    accept_term=(By.XPATH," //section[@id='cookiebar']//following::a[normalize-space(text())='Accept Terms']")
    login_link = (By.XPATH, "//span[contains(text(),'Login')]")

    hello_str =(By.XPATH,"//span[contains(text(),'Hello')]")

    header_bom_tool_link = (By.XPATH,"//div[@class='mega-wrapper Content']/ul[@class='megamenu Content']/li[@data-gtm-label='BOM Tool']//a[@href='/en/bom-page']")

    # Access the elements
    logout_link=(By.XPATH,"(//ul[@class='ButtonList']/li/button)[1]") #(//ul[@class='ButtonList']/li/button)[1]

    my_account_link=(By.XPATH,"(//div[@title='My Account'])[1]")



    def get_accept_term_button(self):
        return self.driver.find_element(*self.accept_term)

    def get_login_link(self):
        return self.driver.find_element(*self.login_link)

    def get_hello_str(self):
        return self.driver.find_element(*self.hello_str)

    def get_header_bom_tool_link(self):
        return self.driver.find_element(*self.header_bom_tool_link)

    def get_logout_link(self):
        return self.driver.find_element(*self.logout_link)

    def get_my_account_link(self):
        return self.driver.find_element(*self.my_account_link)


