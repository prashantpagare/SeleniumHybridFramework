import time

from selenium.webdriver.common.by import By

from pageObjects.OC_LoginPage import OC_Login
from pageObjects.OC_HomePage import OC_HomePage
from pageObjects.OC_MyAccountPage import OC_MyAccountPage
from pageObjects.OC_AffiliateInformationPage import OC_AffiliateInformationPage
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_OC_AffiliateInformation:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_OC_AffiliateInformation(self, setup):
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
        self.oc_aip = OC_AffiliateInformationPage(self.driver)

        self.oc_ap.clickOnEditAffiliateAccountInfo()
        self.oc_aip.setCompany("Apple")
        self.oc_aip.setWebsite("https://www.apple.co.in")
        self.oc_aip.setTaxID("848848484akndegfa")
        self.oc_aip.selectPaymentMethod("Cheque")
        self.driver.execute_script("window.scrollTo(0,150);")

        self.oc_aip.setChequePayeeName("Omega")
        self.oc_aip.setChequePayeeName("abc")

        # self.oc_aip.setPaypalEmail("paymepal@pay.com")

        # self.oc_aip.setBankName("HFDC")
        # self.oc_aip.setBranchNumber("987433")
        # self.oc_aip.setSwiftCode("557")
        # self.oc_aip.setAccountName("Donny")
        # self.oc_aip.setAccountNumber("008963")

        time.sleep(5)





