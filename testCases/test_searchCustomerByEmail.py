import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addNewCustomer(self, setup):
        self.logger.info("********** Search Customer By Email test started **********")
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
        self.logger.info("********** Search Customer By Email **********")

        self.sc = SearchCustomer(self.driver)
        self.sc.setEmail("brenda_lindgren@nopCommerce.com")
        self.sc.clickOnSearch()

        time.sleep(3)
        email = self.sc.searchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        print(email)
        assert True == email
        self.logger.info("********** Search Customer By Email test Completed **********")

        self.driver.close()