import time

from pageObjects.LoginPage import LoginPage
from pageObjects.searchProducts import searchProducts
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_006_SearchProductByName:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    def test_searchProductByName(self, setup):
        self.logger.info("********** Search Product By Name test started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setUserPassword(self.password)
        self.lp.clickOnLogin()
        self.logger.info("********** Login Successful **********")

        self.sp = searchProducts(self.driver)
        self.sp.clickOnCatalogMenu()
        self.sp.clickOnCatalogProductMenuItem()
        self.sp.clickOnSeachSubcateory()
        time.sleep(2)
        self.sp.setproductName("Adobe Photoshop CS4")
        self.sp.setCategory("Computers >> Software")
        # self.sp.clickOnSeachSubcateory()
        self.sp.clickOnSearch()
        time.sleep(2)
        product = self.sp.searchProductByName("Adobe Photoshop CS4")
        print(product)
        assert True == product
        self.logger.info("********** Search Product By Name test Completed **********")

        self.driver.close()
