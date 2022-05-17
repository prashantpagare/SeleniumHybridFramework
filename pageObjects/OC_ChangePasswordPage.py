from selenium.webdriver.common.by import By


class OC_ChangePasswordPage:
    inputChangePassword_XPATH = "//input[@id='input-password']"
    inputPasswordConfirm_XPATH ="//input[@id='input-confirm']"
    buttonContinue_XPATH = "//input[@value='Continue']"
    buttonBack_XPATH = "//a[@class='btn btn-default']"

    def __init__(self, driver):
        self.driver = driver


    def setChangePassword(self, passwd):
        self.driver.find_element(By.XPATH, self.inputChangePassword_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputChangePassword_XPATH).send_keys(passwd)

    def setPasswordConfirm(self, passwd):
        self.driver.find_element(By.XPATH, self.inputPasswordConfirm_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputPasswordConfirm_XPATH).send_keys(passwd)

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.buttonContinue_XPATH).click()

    def clickOnBackButton(self):
        self.driver.find_element(By.XPATH, self.buttonBack_XPATH).click()