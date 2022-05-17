from selenium.webdriver.common.by import By


class OC_Login:
    linkmyAccount_XPATH = "//a[@title='My Account']"
    linkLogin_XPATH = "//a[contains(text(),'Login')]"
    inputEmailid_XPATH = "//input[@id='input-email']"
    inputPassword_XPATH = "//input[@id='input-password']"
    buttonLogin_XPATH = "//input[@value='Login']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnMyAccount(self):
        self.driver.find_element(By.XPATH,self.linkmyAccount_XPATH).click()

    def clickOnLoginLink(self):
        self.driver.find_element(By.XPATH,self.linkLogin_XPATH).click()

    def setEmailId(self, emailid):
        self.driver.find_element(By.XPATH,self.inputEmailid_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputEmailid_XPATH).send_keys(emailid)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.inputPassword_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputPassword_XPATH).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element(By.XPATH, self.buttonLogin_XPATH).click()
