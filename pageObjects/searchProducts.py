from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class searchProducts:
    linkCatalogMenu_XPATH = "//p[normalize-space()='Catalog']"
    linkCatalogProductMenuItem_XPATH = "//p[normalize-space()='Products']"
    buttonSearchboxToDisplay_XPATH = "//div[@data-hideattribute='ProductListPage.HideSearchBlock']"
    inputProductName_XPATH = "//input[@id='SearchProductName']"
    drpdownCategory_XPATH = "//select[@id='SearchCategoryId']"
    chkboxseachSubcateory_XPATH = "//input[@id='SearchIncludeSubCategories']"
    button_Search_XPATH = "//button[@id='search-products']"

    table_XPATH = "//table[@id='customers-grid']"
    tableRows_XPATH = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_XPATH = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCatalogMenu(self):
        self.driver.find_element(By.XPATH, self.linkCatalogMenu_XPATH).click()

    def clickOnCatalogProductMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkCatalogProductMenuItem_XPATH).click()

    def clickOnSearchBoxToDisplay(self):
        self.driver.find_element(By.XPATH, self.buttonSearchboxToDisplay_XPATH).click()

    def setproductName(self, product):
        self.driver.find_element(By.XPATH, self.inputProductName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputProductName_XPATH).send_keys(product)

    def setCategory(self, value):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownCategory_XPATH))
        drpdown.select_by_visible_text(value)

    def clickOnSeachSubcateory(self):
        self.driver.find_element(By.XPATH, self.chkboxseachSubcateory_XPATH).click()

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.button_Search_XPATH).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_XPATH))

    def getNoOfColumn(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumn_XPATH))

    def searchProductByName(self, fname):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_XPATH)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            if name == fname:
                flag = True
                break
        return flag
