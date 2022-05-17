import time

from selenium.webdriver.common.by import By

from pageObjects.OC_LoginPage import OC_Login
from pageObjects.OC_HomePage import OC_HomePage
from pageObjects.OC_MyAccountPage import OC_MyAccountPage
from pageObjects.OC_ProductReturnPage import OC_ProductReturnPage
from pageObjects.OC_ProductsReturnPage import OC_ProductsReturnPage
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_OC_OrderHistory:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_OC_OrderHistory(self, setup):
        self.logger.info("********** Verifying Login Test ********** ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = OC_Login(self.driver)
        self.lp.clickOnMyAccount()
        self.lp.clickOnLoginLink()
        self.lp.setEmailId("abc@xyz.com")
        self.lp.setPassword("password")
        self.lp.clickOnLogin()

        self.oc_hp = OC_HomePage(self.driver)
        self.oc_ap = OC_MyAccountPage(self.driver)
        self.oc_psr = OC_ProductsReturnPage(self.driver)


        self.oc_ap.clickOnReturnRequest()
        self.oc_psr.clickOnView("5")
        id = self.driver.find_element(By.XPATH,"//b[normalize-space()='Return ID:']")
        ret = id.find_element(By.XPATH,"//td[contains(text(),'#5')]").text
        print(ret)
        if ret[11:13] == "#5":
            print("ID Matched")
            self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
            self.oc_psr.clickOnContinue()
        else:
            print("ID did not Matched")


        time.sleep(3)


