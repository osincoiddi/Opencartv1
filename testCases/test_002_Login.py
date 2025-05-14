#NOTE: Login page has CAPCHA.
#To execute both test cases, use:pytest -s -v testCases/ -m "sanity"
#NOTE:To execute in cmd, use commands: pytest -m "testCases/ sanity".
import pytest
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGen
import os

class Test_LoginPage():
    baseURL=Readconfig.getApplicationURL()
    # baseURL="https://www.opencart.com/"
    logger=LogGen.loggen()#logger

    # user=Readconfig.getUserEmail()
    # password=Readconfig.getPassword()

    @pytest.mark.sanity
    def test_Login(self,setup):
        self.logger.info("*****start test_002_Login*****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.hp=HomePage(self.driver)


        self.lp=LoginPage(self.driver)
        self.lp.clickLogin()
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.targetpage=self.isMyAcoountPageExist()
        if self.targetpage=="True":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(curdir))+"\\screenshot"+"\\test_login"
            self.driver.close()
            self.logger.info("*****End of test_002_Login****")
            assert False





