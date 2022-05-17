from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class OC_SearchProductPage:
    inputSearchCriteria_XPATH = "//input[@id='input-search']"
    drpdownAllCategory_XPATH = "//select[@name='category_id']"
    chkboxSubCategory_XPATH = "//input[@name='sub_category']"
    chkboxProductDescription_XPATH = "//input[@id='description']"
    buttonSearch_XAPTH = "//input[@id='button-search']"
    listView_XPATH = "//i[@class='fa fa-th-list']"
    gridView_XPATH = "//i[@class='fa fa-th']"
    linkTotalProductCompare_XPATH = "//a[@id='compare-total']"
    drpdownSortBy_XPATH = "//select[@id='input-sort']"
    drpdownShow_XPATH = "//select[@id='input-limit']"
    buttonAddtoCart_XPATH = "//span[normalize-space()='Add to Cart']"
    buttonAddtoWishList_XPATH = "//button[@type='button']//i[@class='fa fa-heart']"
    buttonCompareProduct_XPATH = "//button[@type='button']//i[@class='fa fa-exchange']"
    linkToolTipProcductCompare_XPATH = "//a[normalize-space()='product comparison']"
    ComparethisProduct_XPATH = "//i[@class='fa fa-exchange']"
    linkMacBook_XPATH = "//a[normalize-space()='MacBook']"
    linkiMac_XPATH = "//a[normalize-space()='iMac']"
    linkMacBookAir_XPATH = "//a[normalize-space()='MacBook Air']"
    linkMacBookPro_XPATH = " //a[normalize-space()='MacBook Pro']"
    # linkRedirectProductLink_XPATH = "//a[normalize-space()='MacBook Air']"

    def __init__(self, driver):
        self.driver = driver

    def setSearchCriteria(self, product):
        self.driver.find_element(By.XPATH, self.inputSearchCriteria_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputSearchCriteria_XPATH).send_keys(product)

    def setCategory(self, category):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownAllCategory_XPATH))
        drpdown.select_by_visible_text(category)

    def clickOnSubCategory(self):
        self.driver.find_element(By.XPATH, self.chkboxSubCategory_XPATH).click()

    def clickForProductDesciption(self):
        self.driver.find_element(By.XPATH, self.chkboxProductDescription_XPATH).click()

    def clickOnSearchButton(self):
        self.driver.find_element(By.XPATH, self.buttonSearch_XAPTH).click()

    def gridView(self):
        self.driver.find_element(By.XPATH, self.gridView_XPATH).click()

    def listView(self):
        self.driver.find_element(By.XPATH, self.listView_XPATH).click()

    def sortProducts(self, product):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownSortBy_XPATH))
        drpdown.select_by_visible_text(product)

    def showProductCount(self, product):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownShow_XPATH))
        drpdown.select_by_visible_text(product)

    def clickOnAddtoCart(self):
        self.driver.find_element(By.XPATH, self.buttonAddtoCart_XPATH).click()

    def clickOnAddtoWishList(self):
        self.driver.find_element(By.XPATH, self.buttonAddtoWishList_XPATH).click()

    def clickOnTotalProductCompare(self):
        element = self.driver.find_element(By.XPATH, self.linkTotalProductCompare_XPATH)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()


    def clickOnToolTipProductCompare(self):
        self.driver.find_element(By.XPATH, self.linkToolTipProcductCompare_XPATH).click()

    def clickOnCompareThisProduct(self):
        self.driver.find_element(By.XPATH, self.ComparethisProduct_XPATH).click()

    def clickOnProductName(self, product):
        if product == "iMac":
            self.driver.find_element(By.XPATH, self.linkiMac_XPATH).click()
        elif product == "MacBook":
            self.driver.find_element(By.XPATH, self.linkMacBook_XPATH).click()
        elif product == "MacBookPro":
            self.driver.find_element(By.XPATH, self.linkMacBookPro_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.linkMacBookAir_XPATH).click()