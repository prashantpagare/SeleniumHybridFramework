from selenium.webdriver.common.by import By


class OC_AffiliateInformationPage:
    inputCompany_XPATH = "//input[@id='input-company']"
    inputWebSite_XPATH = "//input[@id='input-website']"
    inputTaxID_XPATH = "//input[@id='input-tax']"
    radioPaymentCheque_XPATH = "//input[@value='cheque']"
    radioPaymentPayPal_XPATH = "//input[@value='paypal']"
    radioPaymentBank_XPATH = "//input[@value='bank']"
    inputChequePayeeName_XPATH ="//input[@id='input-cheque']"
    inputPaypalEmail_XPATH = "//input[@id='input-paypal']"
    inputBankName_XPATH = "//input[@id='input-bank-name']"
    inputBranchNumber_XPATH = "//input[@id='input-bank-branch-number']"
    inputSwiftCode_XPATH = "//input[@id='input-bank-swift-code']"
    inputAccountName_XPATH = "//input[@id='input-bank-account-name']"
    inputAccountNumber_XPATH = "//input[@id='input-bank-account-number']"
    buttonContinue_XPATH = "//input[@value='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def setCompany(self, company):
        self.driver.find_element(By.XPATH, self.inputCompany_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputCompany_XPATH).send_keys(company)

    def setWebsite(self, site):
        self.driver.find_element(By.XPATH, self.inputWebSite_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputWebSite_XPATH).send_keys(site)

    def setTaxID(self, taxid):
        self.driver.find_element(By.XPATH, self.inputTaxID_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputTaxID_XPATH).send_keys(taxid)

    def setChequePayeeName(self, chq):
        self.driver.find_element(By.XPATH, self.inputChequePayeeName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputChequePayeeName_XPATH).send_keys(chq)

    def setPaypalEmail(self, email):
        self.driver.find_element(By.XPATH, self.inputPaypalEmail_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputPaypalEmail_XPATH).send_keys(email)

    def setBankName(self, bname):
        self.driver.find_element(By.XPATH, self.inputBankName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputBankName_XPATH).send_keys(bname)

    def setBranchNumber(self, bnum):
        self.driver.find_element(By.XPATH, self.inputBranchNumber_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputBranchNumber_XPATH).send_keys(bnum)

    def setSwiftCode(self, scode):
        self.driver.find_element(By.XPATH, self.inputSwiftCode_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputSwiftCode_XPATH).send_keys(scode)

    def setAccountName(self, aname):
        self.driver.find_element(By.XPATH, self.inputAccountName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputAccountName_XPATH).send_keys(aname)

    def setAccountNumber(self, anum):
        self.driver.find_element(By.XPATH, self.inputAccountNumber_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputAccountNumber_XPATH).send_keys(anum)

    def selectPaymentMethod(self, method):
        if method == "Cheque":
            self.driver.find_element(By.XPATH, self.radioPaymentCheque_XPATH).click()
            # self.setChequePayeeName(chq)
        elif method == "PayPal":
            self.driver.find_element(By.XPATH, self.radioPaymentPayPal_XPATH).click()
            # self.setPaypalEmail(payemail)
        elif method == "Bank":
            self.driver.find_element(By.XPATH, self.radioPaymentBank_XPATH).click()
            # self.setBankName(bname)
            # self.setBranchNumber(bnumber)
            # self.setSwiftCode(scode)
            # self.setAccountName(aname)
            # self.setAccountNumber(anumber)
        else:
            self.driver.find_element(By.XPATH, self.radioPaymentCheque_XPATH).click()
            # self.setChequePayeeName(chq)

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.buttonContinue_XPATH).click()