from selenium.webdriver.common.by import By


class OC_OrderInformationPage:
    table_XPATH = "//div[@class='table-responsive']"
    tableRows_XPATH = "//div[@class='table-responsive']/table/tbody/tr"
    tableReorder_XPATH = "//div[@class='table-responsive']/table/tbody/tr/td[6]/a[1]"
    tableReturn_XPATH = "//div[@class='table-responsive']/table/tbody/tr/td[6]/a[2]"
    buttonContinue_XPATH = "//a[normalize-space()='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_XPATH))

    def clickOnReorder(self, productName):
            flag = False
            for r in range(1, self.getNoOfRows() + 1):
                table = self.driver.find_element(By.XPATH, self.table_XPATH)
                reOrder = table.find_element(By.XPATH, "table/tbody/tr[" + str(r) + "]/td[6]/a[1]")
                prodName = table.find_element(By.XPATH, "table/tbody/tr[" + str(r) + "]/td[1]").text
                if prodName == productName:
                    reOrder.click()
                    break
            return flag

    def clickOnReturn(self, productName):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_XPATH)
            reOrder = table.find_element(By.XPATH, "table/tbody/tr[" + str(r) + "]/td[6]/a[2]")
            prodName = table.find_element(By.XPATH, "table/tbody/tr[" + str(r) + "]/td[1]").text
            if prodName == productName:
                reOrder.click()
                break
        return flag

