from selenium.webdriver.common.by import By


class OC_ProductComparisonPage:
    linkProductRedirectPage_XPATH = "//strong[normalize-space()='MacBook']"
    inputAddtoCart_XPATH = "//input[@value='Add to Cart']"
    inputSpecificAddtoCart_XPATH = "//table[@class='table table-bordered']/tbody[4]/tr/td[2]/input"
    buttonRemove_XPATH= "//a[normalize-space()='Remove']"
    buttonSpecificRemove_XPATH= "//table[@class='table table-bordered']/tbody[4]/tr/td[2]/a"
    linkHomeBreadcrumb_XPATH = "//i[@class='fa fa-home']"
    linkClickOnEmptyCartContinue_XPATH = "//a[normalize-space()='Continue']"



    def __init__(self, driver):
        self.driver = driver

    def NavigateToProductPage(self):
        self.driver.find_element(By.XPATH,self.linkProductRedirectPage_XPATH).click()

    def clickOnAddToCart(self):
        self.driver.find_element(By.XPATH,self.inputAddtoCart_XPATH).click()

    def clickOnRemoveProduct(self):
        self.driver.find_element(By.XPATH,self.buttonRemove_XPATH).click()

    def ClickOnEmptyCartContinue(self):
        self.driver.find_element(By.XPATH,self.linkClickOnEmptyCartContinue_XPATH).click()