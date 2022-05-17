import time
from pageObjects.OC_LoginPage import OC_Login
from pageObjects.OC_HomePage import OC_HomePage
from pageObjects.OC_MyAccountPage import OC_MyAccountPage
from pageObjects.OC_AddressBook import OC_AddressBookPage
from pageObjects.OC_EditAddress import OC_AddAddressPage
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_OC_AddressBook:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_OC_ModifyAddressBook(self, setup):
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
        self.oc_cp = OC_AddressBookPage(self.driver)
        self.oc_aa = OC_AddAddressPage(self.driver)

        # self.oc_hp.clickOnMyAccount()
        # time.sleep(3)

        self.oc_ap.clickOnModifyAddressBook()
        self.oc_cp.clickOnEditAddress("random")


        time.sleep(3)

