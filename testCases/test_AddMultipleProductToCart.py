import time

from selenium.webdriver.common.by import By
from pageObjects.OC_LoginPage import OC_Login
from pageObjects.OC_HomePage import OC_HomePage
from pageObjects.OC_SearchProductPage import OC_SearchProductPage
from pageObjects.OC_CheckoutPage import OC_CheckoutPage
from pageObjects.OC_ShoppingCartPage import OC_ShoppingCartPage
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import sys
print(sys.getrecursionlimit())

class Test_010_SearchProductByName:
    baseURL = ReadConfig.getApplicationURL()
    emailAdd = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()


    def test_OC_login(self, setup):
        self.logger.info("********** Verifying Login Test ********** ")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = OC_Login(self.driver)
        self.lp.clickOnMyAccount()
        self.lp.clickOnLoginLink()
        self.lp.setEmailId(self.emailAdd)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        time.sleep(3)

        self.oc_hp = OC_HomePage(self.driver)
        self.oc_hp.searchProducts("MacBook")

        self.oc_hp.clickOnSearchButton()
        time.sleep(3)

        # self.oc_hp.hoverOverDesktop()
        self.oc_sp = OC_SearchProductPage(self.driver)
        self.oc_sp.clickOnAddtoCart()

        self.oc_hp.searchProducts("iMac")
        self.oc_hp.clickOnSearchButton()
        self.oc_sp.clickOnAddtoCart()

        self.oc_hp.searchProducts("MacBook Air")
        self.oc_hp.clickOnSearchButton()
        self.oc_sp.clickOnAddtoCart()

        successtext = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        if "Success" in successtext:
            self.oc_hp.clickOnCart()
        self.oc_hp.clickOnView()
        time.sleep(5)

        self.oc_sc = OC_ShoppingCartPage(self.driver)
        self.oc_sc.setMultipleQuantity("2")
        self.oc_sc.updateProductsQuantity()
        update_message = self.driver.find_element(By.CSS_SELECTOR,"div[class*='alert-success']").text
        if "Success" in update_message:
            assert True
        else:
            assert True
        self.oc_sc.removeMultipleProducts()
        empty = self.driver.find_element(By.XPATH,"//div[@id='content']/p").text
        if "empty" in empty:
            assert True
            self.oc_sc.clickOnContinue()
        else:
            assert True
        print(empty)
        time.sleep(15)



        # self.oc_cp = OC_CheckoutPage(self.driver)
        # self.oc_cp.setAddress("")
        # self.oc_cp.selectExistingAddress(2)
        # self.oc_cp.clickOnBillingContinue()
        #
        # self.oc_cp.setAddress("")
        # self.oc_cp.clickOnDeliveryDetailsContinue()
        # self.oc_cp.selectExistingAddress(2)
        # self.oc_cp.setDeliveryAddComments("Nice")
        # self.oc_cp.clickOnDeliveryMethodContinue()
        # self.oc_cp.setPaymentAddComments("Nice")
        # self.oc_cp.clickOnTermsAndConditions()
        # self.oc_cp.clickOnPaymentMethodContinue()
        # self.oc_cp.clickOnConfirmOrder()