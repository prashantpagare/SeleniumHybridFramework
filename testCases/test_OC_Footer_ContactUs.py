import time

from pageObjects.OC_HomePage import OC_HomePage
from pageObjects.OC_ContactUsPage import OC_ContactUsPage
from pageObjects.OC_LoginPage import OC_Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_OC_Footer_ContactUs:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUserEmail()
    passwd = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    def test_OC_Footer_ContactUs(self,setup):
        self.logger.info("********** Verifying Login Test ********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = OC_Login(self.driver)
        self.lp.clickOnMyAccount()
        self.lp.clickOnLoginLink()
        self.lp.setEmailId(self.email)
        self.lp.setPassword(self.passwd)
        self.lp.clickOnLogin()

        self.cu = OC_ContactUsPage(self.driver)
        self.hp = OC_HomePage(self.driver)

        self.driver.execute_script("window.scrollTo(0,200);")
        time.sleep(5)
        self.hp.clickOnFooterContactUs()
        self.cu.setYourFullName("Soul")
        self.cu.setEmailAddress("soul@mol.com")
        self.cu.setEnquiry("I am updating...")
        self.cu.clickOnSubmit()
        time.sleep(5)
