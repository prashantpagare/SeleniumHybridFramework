import time

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.OC_LoginPage import OC_Login
from pageObjects.OC_SearchProductPage import OC_SearchProductPage
from pageObjects.OC_HomePage import OC_HomePage
from pageObjects.ProductDisplayPage import OC_ProductDisplayPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_12_ProductDisplay:
    baseURL = ReadConfig.getApplicationURL()
    emailAdd = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    def test_ProductDisplay(self, setup):
        self.logger.info("********** Verifying Login Test ********** ")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = OC_Login(self.driver)
        self.lp.clickOnMyAccount()
        self.lp.clickOnLoginLink()
        self.lp.setEmailId(self.emailAdd)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()

        self.oc_hp = OC_HomePage(self.driver)
        self.oc_pd = OC_ProductDisplayPage(self.driver)
        self.oc_sp = OC_SearchProductPage(self.driver)

        self.oc_hp.searchProducts("ip")
        self.oc_hp.clickOnSearchButton()
        self.oc_sp.gridView()
        self.driver.execute_script("window.scrollTo(0,250);")

        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")
        for prod in products:
            try:
                productName = prod.find_element(By.XPATH,"div[2]/div/h4/a").text
                if productName == "iPod Touch":
                    prod.find_element(By.XPATH,"div[2]/div/h4/a").click()
            except StaleElementReferenceException as e:
                print(e)
                # ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
                # wait = WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions) \
                #     .until(EC.presence_of_element_located((By.XPATH, element)))
                # self.driver.execute_script("arguments[0].click();", wait)
                # prod.find_element(By.XPATH, "div[2]/div/h4/a").click()

        # self.oc_pd.clickOnAddToWishList()
        # self.oc_pd.clickOnCompareProduct()
        # self.oc_pd.setProductQuantity("5")
        # self.oc_pd.clickOnAddToCart()
        time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0,250);")
        # self.oc_pd.clickOnProductSpecification()
        # self.oc_pd.clickOnProductDescription()
        #
        # self.oc_pd.clickOnWriteReview()
        # self.driver.execute_script("window.scrollTo(0,150);")
        # self.oc_pd.setYourName("John")
        # self.oc_pd.setYourReview("Average Apple Product")
        # self.oc_pd.setRating("4")
        #
        # successReview = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        # print(successReview)
        # time.sleep(3)
        #
        self.oc_pd.clickOnRightArrowKey()
        time.sleep(1)
        # self.driver.execute_script("window.scrollTo(0,0);")
