import pytest

from pageObjects.OC_RegisterPage import OC_Register
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import DDTLogic


class Test_008_OC_Register:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()



    @pytest.mark.parametrize("firstname,lastname,emailAdd,teleNo,passwd,confirmpasswd",
                             DDTLogic.get_userData("Sheet1"))
    def test_OC_RegisterNewAccount(self, setup,firstname,lastname,emailAdd,teleNo,passwd,confirmpasswd):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.register = OC_Register(self.driver)
        self.register.clickOnMyAccount()
        self.register.clickOnRegister()
        self.register.fillForm(firstname,lastname,emailAdd,teleNo,passwd,confirmpasswd)
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
