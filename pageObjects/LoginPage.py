from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_XPATH="//input[@id='Email']"
    textbox_password_XPATH = "//input[@id='Password']"
    checkbox_rememberMe_XPATH="//input[@id='RememberMe']"
    button_login_XPATH="//button[@type='submit']"
    link_logout_XPATH="//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH,self.textbox_username_XPATH).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_XPATH).send_keys(username)

    def setUserPassword(self, password):
        self.driver.find_element(By.XPATH,self.textbox_password_XPATH).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_XPATH).send_keys(password)

    def clickOnRememberMe(self):
        self.driver.find_element(By.XPATH,self.checkbox_rememberMe_XPATH).click()

    def clickOnLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_XPATH).click()

    def clickOnLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_XPATH).click()
