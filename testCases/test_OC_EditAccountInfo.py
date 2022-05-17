import time
from pageObjects.OC_LoginPage import OC_Login
from pageObjects.OC_HomePage import OC_HomePage
from pageObjects.OC_MyAccountPage import OC_MyAccountPage
from pageObjects.OC_MyAccountInformationPage import OC_MyAccountInformationPage
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_OC_EditAccountInfo(self, setup):
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
        self.oc_ai = OC_MyAccountInformationPage(self.driver)

        # self.oc_hp.clickOnMyAccount()
        # time.sleep(3)
        self.oc_ap.clickOnEditAccountInfo()
        self.oc_ai.setFirstname("Mortal")
        self.oc_ai.setLastname("Soul")
        self.oc_ai.setTelephoneNumber("9868963520")
        self.oc_ai.clickOnContinue()

