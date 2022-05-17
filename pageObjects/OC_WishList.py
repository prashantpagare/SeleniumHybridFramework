from selenium.webdriver.common.by import By


class OC_WishList:
    imgProductRedirect_XPATH = "//div[@class='table-responsive']/table/tbody/tr[1]/td[@class='text-center']/a"
    linkProductRedirect_XPATh = "//div[@class='table-responsive']/table/tbody/tr[1]/td[@class='text-left']/a"
    buttonAddToCart_XPATH = "//div[@class='table-responsive']/table/tbody/tr[1]/td[6]/button"
    buttonRemoveProduct_XPATH = "//div[@class='table-responsive']/table/tbody/tr[1]/td[6]/a"
    buttonContinue_XPATH = "//a[@class='btn btn-primary']"
    table_XPATH = "//div[@class='table-responsive']"
    tableRows_XPATH = "//div[@class='table-responsive']/table/tbody/tr"
    tableColumn_XPATH = "//div[@class='table-responsive']/table/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def clickOnImageToRedirect(self):
        self.driver.find_element(By.XPATH, self.imgProductRedirect_XPATH).click()

    def clickOnProductToRedirect(self):
        self.driver.find_element(By.XPATH, self.linkProductRedirect_XPATh).click()

    def clickOnAddToCart(self):
        self.driver.find_element(By.XPATH, self.buttonAddToCart_XPATH).click()

    def clickOnRemoveProduct(self):
        self.driver.find_element(By.XPATH, self.buttonRemoveProduct_XPATH).click()

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.buttonContinue_XPATH).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_XPATH))

    def getNoOfColumn(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumn_XPATH))

    def clickProductToRedirect(self, products):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_XPATH)
            prod = table.find_element(By.XPATH, "table/tbody/tr[" + str(r) + "]/td[2]").text
            print(prod)
            cartbutton = table.find_element(By.XPATH, "table/tbody/tr[" + str(r) + "]/td[6]/button")
            if prod == products:
                print(products)
                cartbutton.click()
                flag = True
                break
        return flag

    def removeProductFromWishlist(self, products):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_XPATH)
            prod = table.find_element(By.XPATH, "table/tbody/tr[" + str(r) + "]/td[2]").text
            print(prod)
            cartbutton = table.find_element(By.XPATH, "table/tbody/tr[" + str(r) + "]/td[6]/a")
            if prod == products:
                print(products)
                cartbutton.click()
                flag = True
                break
        print("Product Not Found")
        return flag
