from selenium.webdriver.common.by import By


class OC_MyAccountInformationPage:
    inputFirstName_XPATH = "//input[@id='input-firstname']"
    inputLastName_XPATH = "//input[@id='input-lastname']"
    inputEmail_XPATH = "//input[@id='input-email']"
    inputTelephone_XPATH = "//input[@id='input-telephone']"
    buttonContinue_XPATH = "//input[@value='Continue']"
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

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.buttonContinue_XPATH).click()

    def clickOnBackButton(self):
        self.driver.find_element(By.XPATH, self.buttonBack_XPATH).click()