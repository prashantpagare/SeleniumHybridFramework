from selenium.webdriver.common.by import By


class OC_MyAccountPage:
    linkEditAccountInfo_XPATH = "//a[normalize-space()='Edit your account information']"
    linkChangePassword_XPATH = "//a[normalize-space()='Change your password']"
    linkModifyAddressBook_XPATH = "//a[normalize-space()='Modify your address book entries']"
    linkModifyWishlist_XPATH = "//a[normalize-space()='Modify your wish list']"
    linkViewOrderHistory_XPATH = "//a[normalize-space()='View your order history']"
    linkDownloads_XPATH = "//ul[@class='list-unstyled']//a[normalize-space()='Downloads']"
    linkYourRewardPoints_XPATH = "//a[normalize-space()='Your Reward Points']"
    linkReturnRequest_XPATH = "//a[normalize-space()='View your return requests']"
    linkYourTransaction_XPATH = "//a[normalize-space()='Your Transactions']"
    linkRecurringPayments_XPATH = "//ul[@class='list-unstyled']//a[normalize-space()='Recurring payments']"
    linkRegisterAffiliateAccount_XPATH = "//a[normalize-space()='Register for an affiliate account']"
    linkEditAffiliateAccountInfo_XPATH = "//a[normalize-space()='Edit your affiliate information']"
    linkSubUnSubNewsletter_XPATH = "//a[normalize-space()='Subscribe / unsubscribe to newsletter']"

    linkRightMyAccount_XPATH = "//a[@class='list-group-item'][normalize-space()='My Account']"
    linkRightEditAccount_XPATH = "//a[normalize-space()='Edit Account']"
    linkRightPassword_XPATH = "//a[normalize-space()='Password']"
    linkRightAddressBook_XPATH = "//a[normalize-space()='Address Book']"
    linkRightWishList_XPATH = "//a[@class='list-group-item'][normalize-space()='Wish List']"
    linkRightOrderHistory_XPATH = "//a[@class='list-group-item'][normalize-space()='Order History']"
    linkRightDownloads_XPATH = "//a[@class='list-group-item'][normalize-space()='Downloads']"
    linkRightRecurringPayments_XPATH = "//a[@class='list-group-item'][normalize-space()='Recurring payments']"
    linkRightRewardPoints_XPATH = "//a[normalize-space()='Reward Points']"
    linkRightReturns_XPATH = "//a[@class='list-group-item'][normalize-space()='Returns']"
    linkRightTransactions_XPATH = "//a[@class='list-group-item'][normalize-space()='Transactions']"
    linkRightNewsletter_XPATH = "//a[@class='list-group-item'][normalize-space()='Newsletter']"
    linkRightLogout_XPATH = "//a[@class='list-group-item'][normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnEditAccountInfo(self):
        self.driver.find_element(By.XPATH,self.linkEditAccountInfo_XPATH).click()

    def clickOnChangePassword(self):
        self.driver.find_element(By.XPATH,self.linkChangePassword_XPATH).click()

    def clickOnModifyAddressBook(self):
        self.driver.find_element(By.XPATH,self.linkModifyAddressBook_XPATH).click()

    def clickOnModifyWishlist(self):
        self.driver.find_element(By.XPATH,self.linkModifyWishlist_XPATH).click()

    def clickOnViewOrderHistory(self):
        self.driver.find_element(By.XPATH,self.linkViewOrderHistory_XPATH).click()

    def clickOnDownloads(self):
        self.driver.find_element(By.XPATH,self.linkDownloads_XPATH).click()

    def clickOnYourRewardPoints(self):
        self.driver.find_element(By.XPATH,self.linkYourRewardPoints_XPATH).click()

    def clickOnReturnRequest(self):
        self.driver.find_element(By.XPATH,self.linkReturnRequest_XPATH).click()

    def clickOnYourTransaction(self):
        self.driver.find_element(By.XPATH,self.linkYourTransaction_XPATH).click()

    def clickOnRecurringPayments(self):
        self.driver.find_element(By.XPATH,self.linkRecurringPayments_XPATH).click()

    def clickOnRegisterAffilicateAccount(self):
        self.driver.find_element(By.XPATH,self.linkRegisterAffiliateAccount_XPATH).click()

    def clickOnEditAffiliateAccountInfo(self):
        self.driver.find_element(By.XPATH, self.linkEditAffiliateAccountInfo_XPATH).click()

    def clickOnSubUnSubNewsletter(self):
        self.driver.find_element(By.XPATH,self.linkSubUnSubNewsletter_XPATH).click()

    def NavigateToMyAccount(self):
        self.driver.find_element(By.XPATH, self.linkRightMyAccount_XPATH).click()

    def NavigateToEditAccount(self):
        self.driver.find_element(By.XPATH, self.linkRightEditAccount_XPATH).click()

    def NavigateToPassword(self):
        self.driver.find_element(By.XPATH, self.linkRightPassword_XPATH).click()

    def NavigateToAddressBook(self):
        self.driver.find_element(By.XPATH, self.linkRightAddressBook_XPATH).click()

    def NavigateToWishList(self):
        self.driver.find_element(By.XPATH, self.linkRightWishList_XPATH).click()

    def NavigateToOrderHistory(self):
        self.driver.find_element(By.XPATH, self.linkRightOrderHistory_XPATH).click()

    def NavigateToDownloads(self):
        self.driver.find_element(By.XPATH, self.linkRightDownloads_XPATH).click()

    def NavigateToRecurringPayments(self):
        self.driver.find_element(By.XPATH, self.linkRightRecurringPayments_XPATH).click()

    def NavigateToRewardPoints(self):
        self.driver.find_element(By.XPATH, self.linkRightRewardPoints_XPATH).click()

    def NavigateToReturns(self):
        self.driver.find_element(By.XPATH, self.linkRightReturns_XPATH).click()

    def NavigateToTransactions(self):
        self.driver.find_element(By.XPATH, self.linkRightTransactions_XPATH).click()

    def NavigateToNewsletter(self):
        self.driver.find_element(By.XPATH, self.linkRightNewsletter_XPATH).click()

    def clickOnLogout(self):
        self.driver.find_element(By.XPATH, self.linkRightLogout_XPATH).click()