#NOTE: Login page has CAPCHA.
#To execute both test cases, use:pytest -s -v testCases/ -m "sanity"
#NOTE:To execute in cmd, use commands: pytest -m "testCases/ sanity".
import pytest
from selenium import webdriver
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_LoginPage():
    baseURL="https://www.opencart.com/"
    # baseURL = Readconfig.getApplicationURL()
    logger=LogGen.loggen()#logger

    # user=Readconfig.getEmail()
    # password=Readconfig.getPassword()

    @pytest.mark.sanity
    def test_Login(self,setup):
        self.logger.info("*****start test_002_Login*****")
        self.driver=setup
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.opencart.com/")
        # self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp=HomePage(self.driver)


        self.lp=LoginPage(self.driver)
        # self.lp.clickFirstLoginBtn()
        self.lp.setEmail("tiyumiddi@gmail.com")
        self.lp.setPassword("Kugazugu2014")
        self.lp.clickLogin()
        self.targetpage=self.isMyAcoountPageExist()
        if self.targetpage=="True":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(curdir))+"\\screenshot"+"\\test_login"
            self.driver.close()
            self.logger.info("*****End of test_002_Login****")
            assert False





