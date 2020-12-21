import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def testHomepageTitle(self,setup):

        self.logger.info("*****Test_001_Login*****")
        self.logger.info("*****Verifying Home Page*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title=='Your store. Login':
            assert True
            self.logger.info("*****Home page title is passed*****")
        else:
            assert False
            self.logger.error("*****Home page title is failed*****")

    def testLogin(self,setup):
        self.logger.info("*****Test case2 Verifying login test*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False
