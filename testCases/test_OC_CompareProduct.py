import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.OC_LoginPage import OC_Login
from pageObjects.OC_SearchProductPage import OC_SearchProductPage
from pageObjects.OC_HomePage import OC_HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_11_CompareProduct:
    baseURL = ReadConfig.getApplicationURL()
    emailAdd = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    def test_CompareProduct(self, setup):
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

        self.logger.info("********** Verifying CompareProduct Test ********** ")
        self.oc_hp = OC_HomePage(self.driver)
        self.oc_sp = OC_SearchProductPage(self.driver)
        self.oc_hp.searchProducts("mac")
        self.oc_hp.clickOnSearchButton()
        self.oc_sp.listView()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        compare_products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")

        for product in compare_products:
            prodName = product.find_element(By.XPATH, "div/div/h4/a").text
            if prodName == "MacBook Pro":
                product.find_element(By.XPATH, "div/div[2]/button[3]").click()
                successtext = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
                if "Success" in successtext:
                    wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//a[@id='compare-total']")))
                    self.driver.execute_script("arguments[0].click();", wait)
                    # self.oc_sp.clickOnTotalProductCompare()

                    title = self.driver.title
                    if title == "Product Comparison":
                        assert True
                        time.sleep(2)
                        self.driver.close()
                    else:
                        self.driver.save_screenshot((".\\Screenshots\\" + "test_ProductCompare.png"))
                        self.driver.close()
                        self.logger.error("**********  ProductCompare Page Title test is failed ********** ")
                        assert False
