from selenium.webdriver.common.by import By


class OC_GiftCertificatePage:
    inputRecipientName_XPATH = "//input[@id='input-to-name']"
    inputRecipientEmail_XPATH = "//input[@id='input-to-email']"
    inputYourName_XPATH = "//input[@id='input-from-name']"
    inputEmailAddress_XPATH = "//input[@id='input-from-email']"
    radioGCThemeBirthday_XPATH = "//input[@value='7']"
    radioGCThemeChristmas_XPATH = "//input[@value='6']"
    radioGCThemeGeneral_XPATH = "//input[@value='8']"
    inputMessage_XPATH = "//textarea[@id='input-message']"
    inputAmount_XPATH = "//input[@id='input-amount']"
    chkboxTermsConditions_XPATH = "//input[@name='agree']"
    buttonContinue_XPATH = "//input[@value='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def setRecipientName(self, name):
        self.driver.find_element(By.XPATH, self.inputRecipientName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputRecipientName_XPATH).send_keys(name)

    def setRecipientEmail(self, email):
        self.driver.find_element(By.XPATH, self.inputRecipientEmail_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputEmailAddress_XPATH).send_keys(email)

    def setYourFullName(self, name):
        self.driver.find_element(By.XPATH, self.inputYourName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputYourName_XPATH).send_keys(name)

    def setEmailAddress(self, email):
        self.driver.find_element(By.XPATH, self.inputEmailAddress_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputEmailAddress_XPATH).send_keys(email)

    def selectGCTheme(self, theme):
        if theme == "Birthday":
            self.driver.find_element(By.XPATH, self.radioGCThemeBirthday_XPATH).click()
        elif theme == "Christmas":
            self.driver.find_element(By.XPATH, self.radioGCThemeChristmas_XPATH).click()
        elif theme == "General":
            self.driver.find_element(By.XPATH, self.radioGCThemeGeneral_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.radioGCThemeGeneral_XPATH).click()

    def setMessage(self, mess):
        self.driver.find_element(By.XPATH, self.inputMessage_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputMessage_XPATH).send_keys(mess)

    def setAmount(self, amount):
        self.driver.find_element(By.XPATH, self.inputAmount_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputAmount_XPATH).send_keys(amount)

    def clickOnTermsConditions(self):
        self.driver.find_element(By.XPATH, self.chkboxTermsConditions_XPATH).click()

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.buttonContinue_XPATH).click()
