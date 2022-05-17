from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class OC_AddAddressPage:
    inputFirstName_XPATH = "//input[@id='input-firstname']"
    inputLastName_XPATH = "//input[@id='input-lastname']"
    inputCompany_XPATH = "//input[@id='input-company']"
    inputAddress1_XPATH = "//input[@id='input-address-1']"
    inputAddress2_XPATH = "//input[@id='input-address-2']"
    inputCity_XPATH = "//input[@id='input-city']"
    inputPostalCode_XPATH = "//input[@id='input-postcode']"
    drpdownCountry_XPATH = "//select[@id='input-country']"
    drpdownState_XPATH = "//select[@id='input-zone']"
    radioDefaultAddressYes_XPATH = "//input[@value='1']"
    radioDefaultAddressNo_XPATH = "//input[@value='0']"
    buttonContinue_XPATH = "//input[@value='Continue']"
    buttonBack_XPATH = "//a[@class='btn btn-default']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.inputFirstName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputFirstName_XPATH).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.inputLastName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputLastName_XPATH).send_keys(lname)

    def setCompanyName(self, company):
        self.driver.find_element(By.XPATH, self.inputCompany_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputCompany_XPATH).send_keys(company)

    def setAddress1(self, add1):
        self.driver.find_element(By.XPATH, self.inputAddress1_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputAddress1_XPATH).send_keys(add1)

    def setAddress2(self, add2):
        self.driver.find_element(By.XPATH, self.inputAddress2_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputAddress2_XPATH).send_keys(add2)

    def setCity(self, city):
        self.driver.find_element(By.XPATH, self.inputCity_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputCity_XPATH).send_keys(city)

    def setPostCode(self, pcode):
        self.driver.find_element(By.XPATH, self.inputPostalCode_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputPostalCode_XPATH).send_keys(pcode)

    def selectCountry(self, country):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownCountry_XPATH))
        drpdown.select_by_visible_text(country)

    def selectState(self, state):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownState_XPATH))
        drpdown.select_by_visible_text(state)

    def setDefaultAddress(self,opt):
        if opt == "Yes":
            self.driver.find_element(By.XPATH, self.radioDefaultAddressYes_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.radioDefaultAddressNo_XPATH).click()

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.buttonContinue_XPATH).click()

    def clickOnBackButton(self):
        self.driver.find_element(By.XPATH, self.buttonBack_XPATH).click()