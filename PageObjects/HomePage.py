from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage():
    #locators
    lnk_register_xpath="//a[@class='btn btn-black navbar-btn']"
    lnk_login_linktxt="Login"

    # #constructor
    def __init__(self,driver):
        self.driver=driver

        #action methods
    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.lnk_register_xpath).click()
        self.driver.find_element(By.XPATH,self.lnk_register_xpath).is_displayed()
        self.driver.switchTo().alert()
        self.driver.alert.accept()


    def clickLogin(self):
         self.driver.find_element(By.XPATH,self.lnk_login_linktxt).click()#needed for login





