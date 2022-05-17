import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.OC_LoginPage import OC_Login
from pageObjects.OC_HomePage import OC_HomePage
from pageObjects.OC_WishList import OC_WishList
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_11_CompareProduct:
    baseURL = ReadConfig.getApplicationURL()
    emailAdd = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    def test_WishListVerification(self, setup):
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
        self.oc_wl = OC_WishList(self.driver)

        self.oc_hp.clickOnHeaderWishList()
        # self.oc_wl.clickProductToRedirect("HP LP3065")
        self.oc_wl.removeProductFromWishlist("MacBook")
        self.oc_wl.clickOnContinue()
        time.sleep(3)

