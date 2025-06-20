#NOTE:This POM was created for data driven test.
#Note that this page object module/class could contain so many elements on a/c page.

from selenium.webdriver.common.by import By

class MyAccountPage():
    #locators
    link_logout_xpath="//a[@class='btn btn-black navbar-btn']"


      #constructor
    def __init__(self,driver):
        self.driver=driver


    #action method
    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()