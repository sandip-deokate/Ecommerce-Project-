#from selenium import webdriver
from selenium.webdriver.common.by import By
#from adodbapi.examples.xls_read import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class webDriverCommonMethods:
    def __init__(self,driver):
        self.driver =driver

    def wait_till_element_clickable(self,element):
       (WebDriverWait(self.driver,30,poll_frequency=2).
                 until(EC.element_to_be_clickable(element)))
       return element

    def wait_till_presence_element_located(self,element):
        mywait= WebDriverWait(self.driver,30,poll_frequency=2)
        mywait.until(EC.presence_of_element_located(element))
        return element

    def scroll_till_element_located(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
