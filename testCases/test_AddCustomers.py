import random
import string

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen




class Test_003_addCustomer:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addNewCustomer(self, setup):
        self.logger.info("********** Add Customer test started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setUserPassword(self.password)
        self.lp.clickOnLogin()
        self.logger.info("********** Login Successful **********")

        self.addcust = AddCustomerPage(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("********** Providing Customer info **********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("125486+")
        self.addcust.setFirstName("abc")
        self.addcust.setLastName("xyz")
        self.addcust.selectGender("Female")
        self.addcust.setDOB("3/8/2000")
        self.addcust.setComapnyName("aaa")
        self.addcust.clickOnTaxExtempt()
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManageVendor("Vendor 2")
        self.addcust.setComment("hello!")
        self.addcust.clickOnSave()
        self.logger.info("********** Saving Customer info **********")

        self.logger.info("********** Validation of  Customer info **********")

        self.msg = self.driver.find_element_by_tag_name("body").text

        if 'customer' in self.msg:
            assert True == True
            self.logger.info("********** Add Customer test passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.info("**********  Add Customer test is Failed ********** ")
            assert True == False

        self.driver.close()
        self.logger.info("**********  Add Customer test is Failed ********** ")


def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))
