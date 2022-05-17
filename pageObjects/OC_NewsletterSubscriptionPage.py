from selenium.webdriver.common.by import By


class OC_NewsletterSubscriptionPage:
    radioSubscribeYes_XPATH = "//input[@value='1']"
    radioSubscribeNo_XPATH = "//input[@value='2']"
    buttonContinue_XPATH = "//input[@value='Continue']"
    buttonBack_XPATH = "//a[@class='btn btn-default']"

    def __init__(self, driver):
        self.driver = driver

    def newsLetterSubscription(self, opt):
        if opt == "Yes":
            self.driver.find_element(By.XPATH, self.radioSubscribeYes_XPATH).click()
        elif opt == "No":
            self.driver.find_element(By.XPATH, self.radioSubscribeNo_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.radioSubscribeYes_XPATH).click()

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.buttonContinue_XPATH).click()

    def clickOnBackButton(self):
        self.driver.find_element(By.XPATH, self.buttonBack_XPATH).click()