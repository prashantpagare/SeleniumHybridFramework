import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class OC_HomePage:
    inputSearchBox_XPATH = "//input[@placeholder='Search']"
    buttonSearch_XAPTH = "//button[@class='btn btn-default btn-lg']"
    buttonShoppingCart_XPATH = "//div[@id='cart']/button[@data-toggle='dropdown']"
    buttonViewCart_XPATH = "//strong[normalize-space()='View Cart']"
    buttonCheckoutCart_XPATH = "//strong[normalize-space()='Checkout']"
    linkHoverDesktop_XPATH = "//a[normalize-space()='Desktops']"
    linkHoverShowAllDesktops_XPATH = "//a[normalize-space()='Show All Desktops']"
    linkHeaderContactUs_XPATH = "//i[@class='fa fa-phone']"
    drpdownHeaderMyAccount_XPATH = "//a[@title='My Account']"
    linkHeaderMyAccount_XPATH = "//span[normalize-space()='My Account']"
    linkSubMenuMyAccount_XPATH = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='My Account']"
    linkSubMenuOrderHistory_XPATH = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Order History']"
    linkSubMenuMyTransactions_XPATH = "//a[normalize-space()='Transactions']"
    linkSubMenuMyDownloads_XPATH = "//a[normalize-space()='Downloads']"
    linkSubMenuMyLogout_XPATH = "//a[normalize-space()='Logout']"
    linkHeaderWishList_XPATH = "//span[starts-with(text(),'Wish List')]"
    linkHeaderShopping_Cart_XPATH = "//span[normalize-space()='Shopping Cart']"
    linkHeaderCheckout_XPATH = "//span[normalize-space()='Checkout']"
    linkYourStoreLogo_XPATH = "//a[normalize-space()='Your Store']"
    drpdownCurrency_XPATH = "//ul[@class='dropdown-menu']"
    linkFooterContact_XPATH = "//a[normalize-space()='Contact Us']"


    def __init__(self, driver):
        self.driver = driver

    def searchProducts(self, product):
        self.driver.find_element(By.XPATH, self.inputSearchBox_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputSearchBox_XPATH).send_keys(product)

    def clickOnSearchButton(self):
        self.driver.find_element(By.XPATH, self.buttonSearch_XAPTH).click()

    def hoverOverDesktop(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,locator )))
        ac = ActionChains(self.driver)
        ac.move_to_element(element).perform()

    def contactUsHeader(self):
        self.driver.find_element(By.XPATH, self.contactUsHeader()).click()

    def setMyAccountSubMenu(self, text):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdownHeaderMyAccount_XPATH))
        drpdown.select_by_visible_text(text)

    def clickOnHeaderShoppingCart(self):
        self.driver.find_element(By.XPATH, self.linkHeaderShopping_Cart_XPATH).click()

    def clickOnHeaderWishList(self):
        # locator = "//span[normalize-space()='Wish List (0)']"
        # li = locator.split("'")
        # wishlist = li[1].startswith("Wish List")
        self.driver.find_element(By.XPATH, self.linkHeaderWishList_XPATH).click()

    def clickOnHeaderCheckout(self):
        self.driver.find_element(By.XPATH, self.linkHeaderCheckout_XPATH).click()

    def clickOnCart(self):
        self.driver.find_element(By.XPATH, self.buttonShoppingCart_XPATH).click()

    def clickOnView(self):
        self.driver.find_element(By.XPATH, self.buttonViewCart_XPATH).click()

    def clickOnCheckout(self):
        self.driver.find_element(By.XPATH, self.buttonCheckoutCart_XPATH).click()

    def _wait_and_click(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.element_to_be_clickable((locator["by"], locator["value"]))).click()
        except TimeoutException:
            return False
        return True

    def clickOnMyAccount(self):
        self.driver.find_element(By.XPATH, self.drpdownHeaderMyAccount_XPATH).click()
        elements = self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']").text
        print(elements)
        for i in elements:
            if i == "Downloads":
                i.click()
                break
            else:
                print("No Click")
                break

    def clickOnFooterContactUs(self):
        self.driver.find_element(By.XPATH, self.linkFooterContact_XPATH).click()


