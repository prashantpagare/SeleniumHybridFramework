import time
from pageObjects.OC_LoginPage import OC_Login
from pageObjects.OC_HomePage import OC_HomePage
from pageObjects.OC_MyAccountPage import OC_MyAccountPage
from pageObjects.OC_ChangePasswordPage import OC_ChangePasswordPage
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_OC_ChangePassword:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_OC_OC_ChangePassword(self, setup):
        self.logger.info("********** Verifying Login Test ********** ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = OC_Login(self.driver)
        self.lp.clickOnMyAccount()
        self.lp.clickOnLoginLink()
        self.lp.setEmailId("abc@xyz.com")
        self.lp.setPassword("passwd")
        self.lp.clickOnLogin()

        self.oc_hp = OC_HomePage(self.driver)
        self.oc_ap = OC_MyAccountPage(self.driver)
        self.oc_cp = OC_ChangePasswordPage(self.driver)

        # self.oc_hp.clickOnMyAccount()
        # time.sleep(3)

        self.oc_ap.clickOnChangePassword()
        self.oc_cp.setChangePassword("password")
        self.oc_cp.setPasswordConfirm("password")
        time.sleep(3)
        self.oc_cp.clickOnContinue()
        time.sleep(3)
