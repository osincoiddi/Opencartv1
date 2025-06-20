#conftest.py is needed for set up the browser types you want to use for testing.Refer to last 2 methods below for the hook.
#A hook in Python is a mechanism that allows users to modify or extend the behavior of a program.--
# It provides a way to insert custom code at specific points in the program's execution flow.
#Hooks are often used for tasks such as debugging, logging, or modifying the program's functionality without changing its core code.
import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime



# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     return driver

#Adding browsers and hooks
@pytest.fixture
def setup(browser):
    if browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        print("Launching edge browser--")
        return driver


    elif browser == "firefox":
        driver: WebDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching firefox browser--")
        return driver
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("Launching chrome browser--")
        return driver


def pytest_addoption(parser):  #this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")#This will return browser value to set up method.


###Generating HTML report########
#Hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project name']='Open cart'
    config._metadata['Module name'] ='CutRegistration'

#Hook to delete/modify environment info for html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)


#Specifying report/folder directory
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\report\\"+datetime.now().strftime("%d-%m-%y %H-%M-%S")+".html"



