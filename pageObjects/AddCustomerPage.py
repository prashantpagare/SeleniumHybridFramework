from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerPage:
    linkCustomer_menu_XPATH = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomer_menuItem_XPATH = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    buttonAddNew_XPATH = "//a[@class='btn btn-primary']"
    inputEmail_XPATH = "//input[@id='Email']"
    inputPassword_XPATH = "//input[@id='Password']"
    inputFirstName_XPATH = "//input[@id='FirstName']"
    inputLastName_XPATH = "//input[@id='LastName']"
    radioMaleGender_XPATH = "//input[@id='Gender_Male']"
    radioFemaleGender_XPATH = "//input[@id='Gender_Female']"
    inputDateOfBirth_XPATH = "//input[@id='DateOfBirth']"
    inputCompany_XPATH = "//input[@id='Company']"
    chkboxTax_XPATH = "//input[@id='IsTaxExempt']"
    inputNewsletter_XPATH = "//div[@class='input-group-append']//div[@role='listbox']"
    listItemCustomerRoles_XPATH = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listItemRegistered_XPATH = "//span[normalize-space()='Registered']"
    listItemAdministrators_XPATH = "//span[normalize-space()='Administrators']"
    listItemForum_Moderators_XPATH = "//span[normalize-space()='Forum Moderators']"
    listItemGuests_XPATH = "//span[normalize-space()='Guests']"
    listItemVendors_XPATH = "//span[normalize-space()='Vendors']"
    drpdownManageVendor_XPATH = "//select[@id='VendorId']"
    inputCommentBox_XPATH = "//textarea[@id='AdminComment']"
    buttonSave_XPATH = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menu_XPATH).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menuItem_XPATH).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.buttonAddNew_XPATH).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.inputEmail_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputEmail_XPATH).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.inputPassword_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputPassword_XPATH).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.inputFirstName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputFirstName_XPATH).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.inputLastName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputLastName_XPATH).send_keys(lname)

    def selectGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.radioMaleGender_XPATH)
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.radioFemaleGender_XPATH)
        else:
            self.driver.find_element(By.XPATH, self.radioMaleGender_XPATH)

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.inputDateOfBirth_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputDateOfBirth_XPATH).send_keys(dob)

    def setComapnyName(self, cname):
        self.driver.find_element(By.XPATH, self.inputCompany_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputCompany_XPATH).send_keys(cname)

    def clickOnTaxExtempt(self):
        self.driver.find_element(By.XPATH, self.chkboxTax_XPATH).click()

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.listItemCustomerRoles_XPATH).click()
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.listItemRegistered_XPATH)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.listItemAdministrators_XPATH)
        elif role == "Guests":
            self.driver.find_element(By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.listItemGuests_XPATH)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.listItemRegistered_XPATH)
        elif role == "Vendor":
            self.listitem = self.driver.find_element(By.XPATH, self.listItemVendors_XPATH)
        else:
            self.driver.find_element(By.XPATH, self.listItemGuests_XPATH)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManageVendor(self, value):
        drpdown = Select(self.drpdownManageVendor_XPATH)
        drpdown.select_by_visible_text(value)

    def setComment(self, comment):
        self.driver.find_element(By.XPATH, self.inputCommentBox_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputCommentBox_XPATH).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.buttonSave_XPATH).click()
