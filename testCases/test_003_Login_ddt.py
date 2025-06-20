#Data driven test
# After logging into open cart.com, test a/c detail elements including logout.
#In this regard however,we used only logout element.
#NOTE: We did not specify test type(@pytest.mark.sanity,regression etc.) in data driven testing b/c it takes time
#unlike normal test cases, refer to test_001_-- and test_002_-- methods.
#Note: always separate data driven test cases, don't lump them to normal test cases since it needs a lot of data.

import time
from os.path import curdir

import pytest
from PageObjects.AccountRegistrationPage import AccountRegistration
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readproperties import Readconfig
import os


class Test_Login_DDT():
    baseURL="https://www.opencart.com"# baseURL=Readconfig.getApplicationURL()


    logger=LogGen.loggen()
    path=os.path.abspath(os.curdir)+ "\\testData\\Opencart_loginData.xlsx"



    def test_Login_ddt(self,setup):
        self.logger.info("***start test_003_Login_ddt***")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status =[] #required to verify final results

        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp=HomePage(self.driver)#HomePage Object class
        self.lp=LoginPage(self.driver)#LoginPage Object class
        self.ma=MyAccountPage(self.driver)#MyAccountPage Object class

        for r in range(2,self.rows+1):
            self.hp.clickLogin()

            self.email=XLUtils.getReadData(self.path,"Sheet1",r,1)
            self.pwd=XLUtils.getReadData(self.path,"Sheet1",r,2)
            self.exp=XLUtils.getReadData(self.path,"Sheet1",r,3)
            self.lp=setEmail(self,email)
            self.lp=setPassword(self,pwd)
            self.lp=clicklogin()
            time.sleep(3)
            self.targetpage=self.lp.isMyAccountPageExist()

            if self.exp=='valid':
                if self.targetpage==True:
                    lst_status.append('pass')
                    self.ma.clickLogOut()
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                if tartgetPage==True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                    self.driver.close()
                    #Final validation
                    if "Fail" not in lst_status:
                        assert True
                    else:
                        self.logger.info("*****End of test_003_Login_ddt***** ")
                        assert False








