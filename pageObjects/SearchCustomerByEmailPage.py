from selenium.webdriver.common.by import By


class SearchCustomer:
    inputEmail_XPATH = "//input[@id='SearchEmail']"
    inputSearchFirstName_XPATH = "//input[@id='SearchFirstName']"
    inputSearchLastName_XPATH = "//input[@id='SearchLastName']"
    inputSearchCompany_XPATH = "//input[@id='SearchCompany']"
    buttonSearch_XPATH = "//button[@id='search-customers']"

    tableSearchResult_XPATH = "//table[@role='grid']"
    table_XPATH = "//table[@id='customers-grid']"
    tableRows_XPATH = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_XPATH = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.inputEmail_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputEmail_XPATH).send_keys(email)

    def searchByFirstname(self, fname):
        self.driver.find_element(By.XPATH, self.inputSearchFirstName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputSearchFirstName_XPATH).send_keys(fname)

    def searchByLastname(self, lname):
        self.driver.find_element(By.XPATH, self.inputSearchLastName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputSearchLastName_XPATH).send_keys(lname)

    def searchBycompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.inputSearchCompany_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputSearchCompany_XPATH).send_keys(companyName)

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.buttonSearch_XPATH).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_XPATH))

    def getNoOfColumn(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumn_XPATH))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_XPATH)
            emailId = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[2]").text
            if emailId == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, fname):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_XPATH)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            if name == fname:
                flag = True
                break
        return flag
