from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class OC_AddressBookPage:
    table_XPATH = "//div[@class='table-responsive']"
    tableRows_XPATH = "//div[@class='table-responsive']/table/tbody/tr"
    tableEditAddress_XPATH = "//div[@class='table-responsive']/table/tbody/tr/td[2]/a[1]"
    tableDeleteAddress_XPATH = "//div[@class='table-responsive']/table/tbody/tr/td[2]/a[2]"
    buttonNewAddress_XPATH = "//a[@class='btn btn-primary']"
    buttonBack_XPATH = "//a[@class='btn btn-default']"

    def __init__(self, driver):
        self.driver = driver

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_XPATH))

    def clickOnEditAddress(self, input_data):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_XPATH)
            print(r)
            extracted_data = table.find_element(By.XPATH("table/tbody/tr[" + str(r) + "]/td[1]/br[1]")).text
            print(extracted_data)
            edBtn = table.find_element(By.XPATH("table/tbody/tr[" + str(r) + "]/td[2]/a[1]"))
            if extracted_data == input_data:
                flag = True
                edBtn.click()
                break
        return flag

        # self.driver.find_element(By.XPATH, self.tableEditAddress_XPATH).click()

    def clickOnDeleteAddress(self, opt):
        self.driver.find_element(By.XPATH, self.tableDeleteAddress_XPATH).click()
        alert = Alert(self.driver)
        if opt == "Yes":
            alert.accept()
        else:
            alert.dismiss()

    def clickOnNewAddress(self):
        self.driver.find_element(By.XPATH, self.buttonNewAddress_XPATH).click()

    def clickOnBackButton(self):
        self.driver.find_element(By.XPATH, self.buttonBack_XPATH).click()
