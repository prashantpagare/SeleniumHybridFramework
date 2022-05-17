from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class OC_CheckoutPage:
    linkBillingDetails_XPATH = "//a[@class='accordion-toggle']"
    inputFirstName_XPATH = "//input[@id='input-payment-firstname']"
    inputLastName_XPATH = "//input[@id='input-payment-lastname']"
    inputCompany_XPATH = "//input[@id='input-payment-company']"
    inputAddress1_XPATH = "//input[@id='input-payment-address-1']"
    inputAddress2_XPATH = "//input[@id='input-payment-address-2']"
    inputCity_XPATH = "//input[@id='input-payment-city']"
    inputPostalCode_XPATH = "//input[@id='input-payment-postcode']"
    drpdownCountry_XPATH = "//select[@id='input-payment-country']"
    drpdownState_XPATH = "//select[@id='input-payment-zone']"
    inputBillingContinue_XPATH = "//input[@id='button-payment-address']"
    radioExistingAddress_XPATH = "//input[@value='existing']"
    drpdownExistingAddress_XPATH = "//select[@name='address_id']"
    radioNewAddress_XPATH = "//input[@value='new']"
    inputDeliveryDetailsContinue_XPATH = "//input[@id='button-shipping-address']"
    inputDeliveryAddComments_XPATH = "//textarea[@name='comment']"
    inputDeliveryMethodContinue_XPATH = "//input[@id='button-shipping-method']"
    inputPaymentAddComments_XPATH = "//div[@id='collapse-payment-method']//textarea[@name='comment']"
    chkboxTermsAndConditions_XPATH = "//input[@name='agree']"
    inputPaymentMethodContinue_XPATH = "//input[@id='button-payment-method']"
    inputConfirmOrder_XPATH = "//input[@id='button-confirm']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnBillingDetails(self):
        self.driver.find_element(By.XPATH,self.linkBillingDetails_XPATH).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH,self.inputFirstName_XPATH).clear()
        self.driver.find_element(By.XPATH,self.inputFirstName_XPATH).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH,self.inputLastName_XPATH).clear()
        self.driver.find_element(By.XPATH,self.inputLastName_XPATH).send_keys(lname)

    def setCompanyName(self, company):
        self.driver.find_element(By.XPATH,self.inputCompany_XPATH).clear()
        self.driver.find_element(By.XPATH,self.inputCompany_XPATH).send_keys(company)

    def setAddress1(self, add1):
        self.driver.find_element(By.XPATH,self.inputAddress1_XPATH).clear()
        self.driver.find_element(By.XPATH,self.inputAddress1_XPATH).send_keys(add1)

    def setAddress2(self, add2):
        self.driver.find_element(By.XPATH,self.inputAddress2_XPATH).clear()
        self.driver.find_element(By.XPATH,self.inputAddress2_XPATH).send_keys(add2)

    def setCity(self, city):
        self.driver.find_element(By.XPATH,self.inputCity_XPATH).clear()
        self.driver.find_element(By.XPATH,self.inputCity_XPATH).send_keys(city)

    def setPostCode(self, pcode):
        self.driver.find_element(By.XPATH,self.inputPostalCode_XPATH).clear()
        self.driver.find_element(By.XPATH,self.inputPostalCode_XPATH).send_keys(pcode)

    def selectCountry(self, country):
        drpdown = Select(self.driver.find_element(By.XPATH,self.drpdownCountry_XPATH))
        drpdown.select_by_visible_text(country)

    def selectState(self, state):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownState_XPATH))
        drpdown.select_by_visible_text(state)

    def clickOnBillingContinue(self):
        self.driver.find_element(By.XPATH,self.inputBillingContinue_XPATH).click()

    def setAddress(self,address):
        if address == "New":
            self.driver.find_element(By.XPATH, self.radioNewAddress_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.radioExistingAddress_XPATH).click()

    def selectExistingAddress(self,add):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownExistingAddress_XPATH))
        drpdown.select_by_index(add)

    def clickOnDeliveryDetailsContinue(self):
        self.driver.find_element(By.XPATH,self.inputDeliveryDetailsContinue_XPATH).click()

    def setDeliveryAddComments(self, comments):
        self.driver.find_element(By.XPATH,self.inputDeliveryAddComments_XPATH).clear()
        self.driver.find_element(By.XPATH,self.inputDeliveryAddComments_XPATH).send_keys(comments)

    def clickOnDeliveryMethodContinue(self):
        self.driver.find_element(By.XPATH,self.inputDeliveryMethodContinue_XPATH).click()

    def setPaymentAddComments(self, comments):
        self.driver.find_element(By.XPATH, self.inputPaymentAddComments_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputPaymentAddComments_XPATH).send_keys(comments)

    def clickOnTermsAndConditions(self):
        self.driver.find_element(By.XPATH,self.chkboxTermsAndConditions_XPATH).click()

    def clickOnPaymentMethodContinue(self):
        self.driver.find_element(By.XPATH,self.inputPaymentMethodContinue_XPATH).click()

    def clickOnConfirmOrder(self):
        self.driver.find_element(By.XPATH,self.inputConfirmOrder_XPATH).click()
