from pageObjects.LoginPage import LoginPage
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLutils


class Test_002_Login_DDT:
    path = ".\\TestData\\LoginData.xlsx"
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********** Verifying Test_002_Login_DDT Test ********** ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)

        self.rows = XLutils.getRowCount(self.path, "Sheet1")

        list_status = []

        for r in range(2, self.rows+1):
            self.user = XLutils.readData(self.path,"Sheet1", r, 1)
            self.password = XLutils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLutils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setUserPassword(self.password)
            self.lp.clickOnLogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** Passed ***** ")
                    self.lp.clickOnLogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***** Failed ***** ")
                    self.lp.clickOnLogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** Failed ***** ")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***** Passed ***** ")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("***** DDT Test Passed ***** ")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** DDT Test Failed ***** ")
            self.driver.close()
            assert False

        self.logger.info("********** Completed Test_002_Login_DDT Test ********** ")
