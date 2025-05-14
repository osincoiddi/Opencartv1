from selenium import webdriver
from selenium.webdriver.common.by import By



class AccountRegistration():
    #locators
    txt_username = "username"
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_country_name = "country"
    txt_password = "password"
    img_house_xpath = "//a[@class='active']//img"
    btn_register_xpath = "//button[@class='btn btn-primary btn-lg btn-block visible-xs-block']"
    txt_msg_conf_xpath = "//h3[normalize-space()='Welcome to OpenCart, your account has been created']"
    btn_cont_xpath ="//a[normalize-space()='Continue']"

    # constructor

    def __init__(self, driver):
        self.driver = driver

        #action methods

    def setUserName(self,username):
        self.driver.find_element(By.NAME,self.txt_username).send_keys(username)

    def setFirstname(self, fname):
         self.driver.find_element(By.NAME, self.txt_firstname).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element(By.NAME, self.txt_lastname).send_keys(lname)

    def setEmail(self, email):
         self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setCountry(self):
        self.driver.find_element(By.NAME, self.txt_country_name).click()

    def setPassword(self, password):
         self.driver.find_element(By.NAME, self.txt_password).send_keys(password)

    def setImage(self):
        self.driver.find_element(By.XPATH, self.img_house_xpath).click()

    def setRegister(self):
         self.driver.find_element(By.XPATH, self.btn_register_xpath).click()
         # self.driver.find_element(By.XPATH,self.btn_cont_xpath).is_displayed()
         # self.driver.switchTo().alert()
         # self.driver.alert.accept()

    def getConfirmationMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_msg_conf_xpath).text
        except:
            None

    def setContinue(self):
        self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()





