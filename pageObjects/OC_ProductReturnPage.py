from selenium.webdriver.common.by import By


class OC_ProductReturnPage:
    inputFirstName_XPATH = "//input[@id='input-firstname']"
    inputLastName_XPATH = "//input[@id='input-lastname']"
    inputEmail_XPATH = "//input[@id='input-email']"
    inputTelephone_XPATH = "//input[@id='input-telephone']"
    inputOrderID_XPATH = "//input[@id='input-order-id']"
    inputOrderDate_XPATH = "//input[@id='input-date-ordered']"
    inputProductName_XPATH = "//input[@id='input-product']"
    inputProductCode_XPATH = "//input[@id='input-model']"
    inputQuantity_XPATH = "//input[@id='input-quantity']"
    radioDeadOnArrival_XPATH = "//label[normalize-space()='Dead On Arrival']//input[@name='return_reason_id']"
    radioFaulty_XPATH = "//input[@value='4']"
    radioOrderError_XPATH = "//input[@value='3']"
    radioSupplyDetails_XPATH = "//input[@value='5']"
    radioReceiveWrongItem_XPATH = "//input[@value='2']"
    radioProductOpenedYes_XPATH = "//label[normalize-space()='Yes']//input[@name='opened']"
    radioProductOpenedNo_XPATH = "//input[@value='0']"
    inputFaultyDetails_XPATH = "//textarea[@id='input-comment']"
    buttonSubmit_XPATH = "//input[@value='Submit']"
    buttonBack_XPATH = "//a[@class='btn btn-default']"


    def __init__(self, driver):
        self.driver = driver

    def setFirstname(self, fname):
        self.driver.find_element(By.XPATH,self.inputFirstName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputFirstName_XPATH).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element(By.XPATH,self.inputLastName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputLastName_XPATH).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.inputEmail_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputEmail_XPATH).send_keys(email)

    def setTelephoneNumber(self, tNo):
        self.driver.find_element(By.XPATH,self.inputTelephone_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputTelephone_XPATH).send_keys(tNo)

    def setOrderID(self, id):
        self.driver.find_element(By.XPATH,self.inputOrderID_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputOrderID_XPATH).send_keys(id)

    def setOrderDate(self, date):
        self.driver.find_element(By.XPATH,self.inputOrderDate_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputOrderDate_XPATH).send_keys(date)

    def setProductName(self, pname):
        self.driver.find_element(By.XPATH,self.inputProductName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputProductName_XPATH).send_keys(pname)

    def setProductCode(self, pcode):
        self.driver.find_element(By.XPATH,self.inputProductCode_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputProductCode_XPATH).send_keys(pcode)

    def setQuantity(self, qty):
        self.driver.find_element(By.XPATH,self.inputQuantity_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputQuantity_XPATH).send_keys(qty)

    def ReasonForReturn(self, reason):
        if reason == "Dead":
            self.driver.find_element(By.XPATH, self.radioDeadOnArrival_XPATH).click()
        elif reason == "Faulty":
            self.driver.find_element(By.XPATH, self.radioFaulty_XPATH).click()
        elif reason == "Order Error":
            self.driver.find_element(By.XPATH, self.radioOrderError_XPATH   ).click()
        elif reason == "SupplyDetails":
            self.driver.find_element(By.XPATH, self.radioSupplyDetails_XPATH).click()
        elif reason == "WrongItem":
            self.driver.find_element(By.XPATH, self.radioReceiveWrongItem_XPATH).click()
        else:
            print("Please Enter Reason for Return")


    def ProductOpened(self, reason):
        if reason == "Yes":
            self.driver.find_element(By.XPATH, self.radioProductOpenedYes_XPATH).click()
        elif reason == "No":
            self.driver.find_element(By.XPATH, self.radioProductOpenedNo_XPATH).click()
        else:
            print("Please Select Reason for Product")

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.buttonSubmit_XPATH).click()

    def clickOnBackButton(self):
        self.driver.find_element(By.XPATH, self.buttonBack_XPATH).click()