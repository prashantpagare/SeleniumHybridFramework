from selenium.webdriver.common.by import By


class OC_OrderHistoryPage:
    table_XPATH = "//div[@class='table-responsive']"
    tableRows_XPATH = "//div[@class='table-responsive']/table/tbody/tr"
    buttonContinue_XPATH = "//a[@class='btn btn-primary']"

    def __init__(self, driver):
        self.driver = driver

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_XPATH))


    def clickOnView(self, ordID):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_XPATH)
            view = table.find_element(By.XPATH, "table/tbody/tr[" + str(r) + "]/td[7]")
            orderID = table.find_element(By.XPATH, "table/tbody/tr[" + str(r) + "]/td[1]").text
            act_data = orderID[1:]
            if act_data == ordID:
                view.click()
                break
        return flag

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.buttonContinue_XPATH).click()