from selenium.webdriver.common.by import By


class OC_ContactUsPage:
    inputYourName_XPATH = "//input[@id='input-name']"
    inputEmailAddress_XPATH = "//input[@id='input-email']"
    inputEnquiry_XPATH = "//textarea[@id='input-enquiry']"
    buttonSubmit_XPATH = "//input[@value='Submit']"

    def __init__(self, driver):
        self.driver = driver

    def setYourFullName(self, name):
        self.driver.find_element(By.XPATH, self.inputYourName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputYourName_XPATH).send_keys(name)

    def setEmailAddress(self, email):
        self.driver.find_element(By.XPATH, self.inputEmailAddress_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputEmailAddress_XPATH).send_keys(email)

    def setEnquiry(self, en):
        self.driver.find_element(By.XPATH, self.inputEnquiry_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputEnquiry_XPATH).send_keys(en)

    def clickOnSubmit(self):
        self.driver.find_element(By.XPATH, self.buttonSubmit_XPATH).click()