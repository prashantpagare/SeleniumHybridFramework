import time
from pageObjects.OC_LoginPage import OC_Login
from pageObjects.OC_HomePage import OC_HomePage
from pageObjects.OC_MyAccountPage import OC_MyAccountPage
from pageObjects.OC_AddressBook import OC_AddressBookPage
from pageObjects.OC_EditAddress import OC_AddAddressPage
from pageObjects.OC_OrderHistory import OC_OrderHistoryPage
from pageObjects.OC_OrderInformationPage import OC_OrderInformationPage
from pageObjects.OC_ProductReturnPage import OC_ProductReturnPage
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
        self.oc_cp = OC_AddressBookPage(self.driver)
        self.oc_aa = OC_AddAddressPage(self.driver)
        self.oc_oh = OC_OrderHistoryPage(self.driver)
        self.oc_oi = OC_OrderInformationPage(self.driver)
        self.oc_pr = OC_ProductReturnPage(self.driver)

        # self.oc_hp.clickOnMyAccount()
        # time.sleep(3)

        self.oc_ap.clickOnViewOrderHistory()
        self.oc_oh.clickOnView("11")
        # self.oc_oi.clickOnReorder("iMac")
        self.oc_oi.clickOnReturn("iMac")
        self.oc_pr.setOrderDate("2022-07-05")
        self.oc_pr.ReasonForReturn("WrongItem")
        self.oc_pr.ProductOpened("Yes")
        time.sleep(3)
        self.oc_pr.clickOnSubmit()

