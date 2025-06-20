#NOTE: Main login btn has a didden xpath.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    #locators
    # login_btn="//*[@id='navbar-collapse-header']/div/a[1]"#element hidden
    txt_email_xpath="//input[@id='input-email']"
    txt_password_xpath="//input[@id='input-password']"
    btn_login_xpath= "//button[@class='btn btn-primary btn-lg hidden-xs']"
    msg_myaccount_xpath= "h2//[text()='My Account']"


    #constractors
    def __init__(self,driver):
        self.driver=driver

     # action methods
    # def clickFirstLoginBtn(self):
    #     self.element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.XPATH))
    #     self.driver.find_element(By.XPATH,self.login_btn).click()


    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
        self.driver.alert.dismiss()

    def isMyAccountPageExist(self):
        try:
            return  self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
        except:
            return False

