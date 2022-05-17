from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class OC_ShoppingCartPage:
    imgRedirect_XAPTH = "//div[@class='table-responsive']//following-sibling::tbody/tr/td/a/img[@class='img-thumbnail']"
    linkproductRedirect_XPATH = "//div[@class='table-responsive']//following-sibling::tbody/tr/td[2]/a"
    inputproductQuantity_XPATH = "//div[@class='table-responsive']//following-sibling::tbody/tr/td[4]/div/input"
    inputMultiproductQuantity_XPATH = "//div[@class='input-group btn-block']/input"
    inputupdateMultiproducts_XPATH= "//div[@class='input-group btn-block']/span/button[1]"
    inputRemoveMultiproducts_XPATH = "////div[@class='input-group btn-block']/span/button[2]"
    buttonproductUpdate_XPATH = "//tbody/tr[1]/td[4]/div[1]/span[1]/button[2]//preceding::button[@type='submit']"
    buttonproductRemove_XPATH = "//tbody/tr[1]/td[4]/div[1]/span[1]/button[2]/i[1]"
    linkCouponCode_XPATH = "//a[@class='accordion-toggle']"
    inputEnterCouponCode_XPATH = "//input[@id='input-coupon']"
    inputApplyCouponCode_XPATH = "//input[@id='button-coupon']"
    linkShippingAndTaxes_XPATH = "//a[normalize-space()='Estimate Shipping & Taxes']"
    drpdownCountry_XPATH = "//select[@id='input-country']"
    drpdownState_XPATH = "//select[@id='input-zone']"
    inputPostalCode_XPATH = "//input[@id='input-postcode']"
    buttonGetQuotes_XPATH = "//button[@id='button-quote']"
    linkGiftCertificate_XPATH = "//a[normalize-space()='Use Gift Certificate']"
    inputGiftCertificate_XPATH = "//input[@id='input-voucher']"
    inputApplyGiftCertificate_XPATH = "//input[@id='button-voucher']"
    linkContinueShopping_XPATH = "//a[@class='btn btn-default']"
    linkCheckout_XPATH = "//a[contains(text(),'Checkout')]"
    linkEmptyCart_XPATH = "//a[@class='btn btn-primary']"
    linkclickOnContinue = "//a[normalize-space()='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnImageToRedirect(self):
        self.driver.find_element(By.XPATH, self.imgRedirect_XAPTH).click()

    def clickOnProductLinkToRedirect(self):
        self.driver.find_element(By.XPATH, self.linkproductRedirect_XPATH).click()

    def setProductQuantity(self, quantity):
        self.driver.find_element(By.XPATH, self.inputproductQuantity_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputproductQuantity_XPATH).send_keys(quantity)

    def setMultipleQuantity(self, quantity):
        # self.driver.find_elements(By.XPATH, self.inputMultiproductQuantity_XPATH).clear()
        multi = self.driver.find_elements(By.XPATH, self.inputMultiproductQuantity_XPATH)
        for i in multi:
            i.clear()
            i.send_keys(quantity)

    def updateProductsQuantity(self):
        self.driver.find_element(By.XPATH, self.buttonproductUpdate_XPATH).click()

    def updateMultipleProducts(self):
        update = self.driver.find_element(By.XPATH, self.updateMultipleProducts()).click()
        for i in update:
            i.click()

    def removeProductsQuantity(self):
        self.driver.find_elements(By.XPATH, self.buttonproductRemove_XPATH).click()


    def removeMultipleProducts(self):
        remove = self.driver.find_elements(By.XPATH, self.removeMultipleProducts())
        for i in remove:
          i.click()

    def clickOnCouponCodeLink(self):
        self.driver.find_element(By.XPATH, self.linkCouponCode_XPATH).click()

    def setCouponCode(self, cc):
        self.driver.find_element(By.XPATH, self.inputEnterCouponCode_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputEnterCouponCode_XPATH).send_keys(cc)

    def clickOnApplyCouponCode(self):
        self.driver.find_element(By.XPATH, self.inputApplyCouponCode_XPATH).click()

    def clickOnShippingTaxesLink(self):
        self.driver.find_element(By.XPATH, self.linkShippingAndTaxes_XPATH).click()

    def selectCountryForShipping(self, country):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownCountry_XPATH))
        drpdown.select_by_visible_text(country)

    def selectStateForShipping(self, state):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownState_XPATH))
        drpdown.select_by_visible_text(state)

    def setPostalCode(self, pcode):
        self.driver.find_element(By.XPATH, self.inputPostalCode_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputPostalCode_XPATH).send_keys(pcode)

    def clickOnGetQuotes(self):
        self.driver.find_element(By.XPATH, self.buttonGetQuotes_XPATH).click()

    def clickOnGiftCertificateLink(self):
        self.driver.find_element(By.XPATH, self.linkGiftCertificate_XPATH).click()

    def setGiftCertificateCode(self, gcode):
        self.driver.find_element(By.XPATH, self.inputGiftCertificate_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputGiftCertificate_XPATH).send_keys(gcode)

    def clickOnApplyGiftCertificate(self):
        self.driver.find_element(By.XPATH, self.inputApplyGiftCertificate_XPATH).click()

    def clickOnContinueShopping(self):
        self.driver.find_element(By.XPATH, self.linkContinueShopping_XPATH).click()

    def clickOnCheckout(self):
        self.driver.find_element(By.XPATH, self.linkCheckout_XPATH).click()

    def clickOnEmptyCart(self):
        self.driver.find_element(By.XPATH, self.linkEmptyCart_XPATH).click()

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.linkclickOnContinue).click()


