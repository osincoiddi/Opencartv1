#class Readconfig(): bracket is only needed if we have many classes and want to  specify parent class.
#In this case however,bracket is optional for the class because we don't have multiple classes.
# @staticmethod is used b/c we can call directly by using the class,no need to create an object.
#
import configparser   #required to read data from config.ini file
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        baseURL=config.get("commonInfo","baseURL")
        return baseURL

    @staticmethod
    def getEmail():
        email=config.get("commonInfo","email")
        return email


    @staticmethod
    def getPassword():
        password=config.get("commonInfo","password")
        return password


