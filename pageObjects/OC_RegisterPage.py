from selenium.webdriver.common.by import By


class OC_Register:
    linkMyaccount_XPATH = "//a[@title='My Account']"
    linkRegister_XPATH = "//a[normalize-space()='Register']"
    inputFirstName_XPATH = "//input[@id='input-firstname']"
    inputLastName_XPATH = "//input[@id='input-lastname']"
    inputEmail_XPATH = "//input[@id='input-email']"
    inputTelephone_XPATH = "//input[@id='input-telephone']"
    inputPassword_XPATH = "//input[@id='input-password']"
    inputConfirmPassword_XPATH = "//input[@id='input-confirm']"
    radioSubscribeYes_XPATH = "//label[normalize-space()='Yes']/input[@name='newsletter']"
    radioSubscribeNo_XPATH = "//label[normalize-space()='No']/input[@name='newsletter']"
    chkboxPrivacyPolicy_XPATH = "//input[@name='agree']"
    buttonContinue_XPATH = "//input[@value='Continue']"
    textErrorValidations_XPATH = "//div[@class='text-danger']"
    linkNavigateToLoginPage_XPATH = "//a[normalize-space()='login page']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMyAccount(self):
        self.driver.find_element(By.XPATH,self.linkMyaccount_XPATH).click()

    def clickOnRegister(self):
        self.driver.find_element(By.XPATH,self.linkRegister_XPATH).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.inputFirstName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputFirstName_XPATH).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.inputLastName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputLastName_XPATH).send_keys(lname)

    def setEmailAddress(self, email):
        self.driver.find_element(By.XPATH, self.inputEmail_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputEmail_XPATH).send_keys(email)

    def setTelephoneNo(self, teleNo):
        self.driver.find_element(By.XPATH, self.inputTelephone_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputTelephone_XPATH).send_keys(teleNo)

    def setPassword(self, passwd):
        self.driver.find_element(By.XPATH, self.inputPassword_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputPassword_XPATH).send_keys(passwd)

    def setConfirmPassword(self, cpass):
        self.driver.find_element(By.XPATH, self.inputConfirmPassword_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputConfirmPassword_XPATH).send_keys(cpass)

    def clickOnSubscribe(self, options):
        if options == "Yes":
            self.driver.find_element(By.XPATH, self.radioSubscribeYes_XPATH).click()
        elif options == "No":
            self.driver.find_element(By.XPATH, self.radioSubscribeNo_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.radioSubscribeYes_XPATH).click()

    def setPrivacyPolicy(self):
        self.driver.find_element(By.XPATH, self.chkboxPrivacyPolicy_XPATH).click()

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.buttonContinue_XPATH).click()


    def fillForm(self,firstname,lastname,emailAdd,teleNo,passwd,confirmpasswd):
        self.setFirstName(firstname)
        self.setLastName(lastname)
        self.setEmailAddress(emailAdd)
        self.setTelephoneNo(teleNo)
        self.setPassword(passwd)
        self.setConfirmPassword(confirmpasswd)






