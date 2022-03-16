import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.SearchCustomerByEmailPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
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
        self.logger.info("********** Search Customer By Name **********")

        self.sc = SearchCustomer(self.driver)
        self.sc.searchByFirstname("Arthur")
        self.sc.searchByLastname("Holmes")
        self.sc.clickOnSearch()

        time.sleep(3)
        name = self.sc.searchCustomerByName("Arthur Holmes")
        assert True == name
        self.logger.info("********** Search Customer By Email test Completed **********")

        self.driver.close()