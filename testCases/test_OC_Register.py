from pageObjects.OC_RegisterPage import OC_Register
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_008_OC_Register:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_OC_RegisterNewAccount(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.register = OC_Register(self.driver)
        self.register.clickOnMyAccount()
        self.register.clickOnRegister()
        self.register.setFirstName("Abc")
        self.register.setLastName("xyz")
        self.register.setEmailAddress("abc@xyz.com")
        self.register.setTelephoneNo("3366998855")
        self.register.setPassword("password")
        self.register.setConfirmPassword("password")
        self.register.clickOnSubscribe("Yes")
        self.register.setPrivacyPolicy()
        self.register.clickOnContinue()

        actTitle = self.driver.title
        if actTitle == "Your Account Has Been Created!":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_oc_register.png")
            self.driver.close()
            assert False
