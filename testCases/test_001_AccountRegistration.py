#NOTE:self.email=randomString.random_string_generator()+"@gmail.com"
#The above is used in utility file to generate new email each time in order to prevent failure
#Note:we can hard code: self.regpage.setEmail("abc@gmail.com"). However, this brings failure as it's used often
#Execute via terminal path: pytest -s  -v testCases/test_001_AccountRegistration.py
#chrome by default: pytest -s  -v testCases/test_001_AccountRegistration.py
#specify browser type if testing multiple browsers.Refer to conftest.py.
#http://localhost:5002/{pytest -s -v testCases/test_001_AccountRegistration.py --browser edge
#{pytest -s -v testCases/test_001_AccountRegistration.py --browser firefox

#(os.path.abspath(os.curdir) is used for screenshot location.
#screenshot is expected in the screenshots file after any failure.
#Need to fix alert/CAPCHA to be able to get screenshots.
#NOTE:baseURL=Readconfig.getApplicationURL()#"https://www.opencart.com/" was replaced.Refer to readproperties.py in utility file
#NOTE:Every action/activity you take, specify a logging statement.Logs are found in log files.

import os #needed for screenshots
import time
from enum import verify
from webbrowser import register

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present

from PageObjects.HomePage import HomePage
from PageObjects.AccountRegistrationPage import AccountRegistration
from PageObjects.LoginPage import LoginPage
from PageObjects.MyAccountPage import MyAccountPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen #for logging


class Test_001_AccountRegistration:
    baseURL="https://www.opencart.com/"#Readconfig.getApplicationURL() can replace the url
    # baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen() #For logging.

    @pytest.mark.regression
    def test_account_reg(self,setup):
     self.logger.info("*** test_001_AccountRegistration started ***")
     self.driver=setup
     self.driver=webdriver.Chrome()#for chrome
     # self.driver.get(self.baseURL)
     self.driver.get("https://www.opencart.com/")
     self.logger.info("Launching application")
     self.driver.maximize_window()
     self.driver.implicitly_wait(10)


     self.hp=HomePage(self.driver)
     self.logger.info("Clicking register to register MyAccount")
     self.hp.clickRegister()

     self.logger.info("Providing customer detail for registration")
     self.regpage=AccountRegistrationPage(self.driver)
     self.regpage.setUsername("")
     self.regpage.setFirstname("Joe")
     self.regpage.setLastname("Adams")
     # self.email=randomString.random_string_generator()+'@gmail.com' #refer to utility file
     # self.regpage.setEmail(self.email)
     self.regpage.setCountry.click()
     self.regpage.setPassword("Kugazugu2014")
     self.regpage.setImage.click()
     self.regpage.setRegister.click()
     self.confmsg=self.regpage.getConfirmationMsg()
     self.driver.close()
     if self.confmsg == "Welcome to OpenCart, your account has been created":
      self.logger.info("Account registration is passed")
      assert True
     else:
      self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg")#test method name is used at the end
      self.logger.error("Account registration is failed")
      self.driver.close()
      self.logger.info("*** test_001_AccountRegistration finished ***")
      assert False


    # self.regpage.setContinue.click()
    # self.driver.close()
