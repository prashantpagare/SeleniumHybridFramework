import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class OC_ProductDisplayPage:
    linkThumbNail_XPATH = "//ul[@class='thumbnails']//li[1]//a[1]"
    buttonAddToWishList_XPATH = "//button[@class='btn btn-default']//i[@class='fa fa-heart']"
    buttonCompareProduct_XPATH = "//button[@class='btn btn-default']//i[@class='fa fa-exchange']"
    inputProductQuantity_XPATH = "//input[@id='input-quantity']"
    buttonAddToCart_XPATH = "//button[@id='button-cart']"
    linkWriteReview_XPATH = "//a[normalize-space()='Write a review']"
    linkDescription_XPATH = "//a[normalize-space()='Description']"
    inputYourName_XPATH = "//input[@id='input-name']"
    inputYourReview_XPATH = "//textarea[@id='input-review']"
    radioRatingVal1_XPATH = "//div[4]//div[1]//input[1]"
    radioRatingVal2_XPATH = "//input[@value='2']"
    radioRatingVal3_XPATH = "//input[@value='3']"
    radioRatingVal4_XPATH = "//input[@value='4']"
    radioRatingVal5_XPATH = "//input[@value='5']"
    buttonContinue_XPATH = "//button[@id='button-review']"
    linkReview_XPATH = "//a[normalize-space()='Reviews (0)']"
    buttonRightArrowKey_XPATH = "//button[@title='Next (Right arrow key)']"
    buttonLeftArrowKey_XPATH = "//button[@title='Previous (Left arrow key)']"
    buttonClose_XPATH = "//button[@title='Close (Esc)']"
    linkProductSpecification_XPATH = "//a[normalize-space()='Specification']"
    tableSpecification_XPATH = "//table[@class='table table-bordered']"
    tableDescription_XPATH = "//div[@class='tab-content']"
    radioAvailableOptionsInSmall_XPATH = "//div[@id='input-option218']//div[1]//label[1]"
    radioAvailableOptionsInMedium_XPATH = "//input[@value='6']"
    radioAvailableOptionsInLarge_XPATH = "//input[@value='7']"
    chkbox_Checkbox1_XPATH= "//input[@value='8']"
    chkbox_Checkbox2_XPATH= "//input[@value='9']"
    chkbox_Checkbox3_XPATH= "//input[@value='10']"
    chkbox_Checkbox4_XPATH= "//input[@value='11']"
    txtbox_text_XPATH = "//input[@id='input-option208']"
    drpdown_SelectColor_XPATH = "//select[@id='input-option217']"
    txtbox_textArea_XPATH = "//textarea[@id='input-option209']"
    button_Upload_XPATH = "//button[@id='button-upload222']"
    button_Date_XPATH = "//div[@class='input-group date']//i[@class='fa fa-calendar']"
    button_Next_XPATH = "//div[@class='bootstrap-datetimepicker-widget dropdown-menu bottom pull-right picker-open']//div[@class='datepicker-days']//th[@class='next'][contains(text(),'›')]"
    button_Day_XPATH = "//td[@class='day active'][normalize-space()='5']"
    thMonthyear_XPATH = "//div[@class='bootstrap-datetimepicker-widget dropdown-menu picker-open bottom pull-right']//th[@class='picker-switch'][normalize-space()='February 2011']"
    inputDate_XPATH = "//input[@id='input-option219']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnProductThumbNail(self):
        self.driver.find_element(By.XPATH,self.linkThumbNail_XPATH).click()

    def clickOnAddToWishList(self):
        self.driver.find_element(By.XPATH,self.buttonAddToWishList_XPATH).click()

    def clickOnCompareProduct(self):
        self.driver.find_element(By.XPATH,self.buttonCompareProduct_XPATH).click()

    def setProductQuantity(self, qty):
        self.driver.find_element(By.XPATH, self.inputProductQuantity_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputProductQuantity_XPATH).send_keys(qty)

    def clickOnAddToCart(self):
        self.driver.find_element(By.XPATH,self.buttonAddToCart_XPATH).click()

    def clickOnWriteReview(self):
        self.driver.find_element(By.XPATH, self.linkWriteReview_XPATH).click()

    def setYourName(self, name):
        self.driver.find_element(By.XPATH, self.inputYourName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputYourName_XPATH).send_keys(name)

    def setYourReview(self, review):
        self.driver.find_element(By.XPATH, self.inputYourReview_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputYourReview_XPATH).send_keys(review)

    def setRating(self,rating):
        if rating == "1":
            self.driver.find_element(By.XPATH, self.radioRatingVal1_XPATH).click()
        elif rating == "2":
            self.driver.find_element(By.XPATH, self.radioRatingVal2_XPATH).click()
        elif rating == "3":
            self.driver.find_element(By.XPATH, self.radioRatingVal3_XPATH).click()
        elif rating == "4":
            self.driver.find_element(By.XPATH, self.radioRatingVal4_XPATH).click()
        elif rating == "5":
            self.driver.find_element(By.XPATH, self.radioRatingVal5_XPATH).click()
        else:
            print("Select Rating")

    def clickOnContinue(self):
        self.driver.find_element(By.XPATH, self.buttonContinue_XPATH).click()

    def clickOnProductDescription(self):
        self.driver.find_element(By.XPATH, self.linkDescription_XPATH).click()
        data = self.driver.find_element(By.XPATH, self.tableSpecification_XPATH)
        print(data.text, end=" ")

    def clickOnProductSpecification(self):
        self.driver.find_element(By.XPATH, self.linkProductSpecification_XPATH).click()
        table = self.driver.find_element(By.XPATH, self.tableSpecification_XPATH)
        print(table.text, end=" ")

    def clickOnRightArrowKey(self):
        thumbnail = self.driver.find_element(By.XPATH, self.linkThumbNail_XPATH)
        thumbnail.click()
        right = self.driver.find_element(By.XPATH, self.buttonRightArrowKey_XPATH)
        totalimages = len(self.driver.find_elements(By.XPATH, "//ul[@class='thumbnails']/li"))
        for images in range(0,totalimages - 1):
            right.click()
            time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_images.png")
        self.driver.find_element(By.XPATH,self.buttonClose_XPATH).click()

    def selectAvailableOptions(self, opt):
        if opt == "Small":
            self.driver.find_element(By.XPATH,self.radioAvailableOptionsInSmall_XPATH).click()
        elif opt == "Med":
            self.driver.find_element(By.XPATH,self.radioAvailableOptionsInMedium_XPATH).click()
        elif opt == "Large":
            self.driver.find_element(By.XPATH,self.radioAvailableOptionsInLarge_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.radioAvailableOptionsInSmall_XPATH).click()

    def selectCheckBox(self, chkbx):
        if chkbx == "chk1":
            self.driver.find_element(By.XPATH, self.chkbox_Checkbox1_XPATH).click()
        elif chkbx == "chk2":
            self.driver.find_element(By.XPATH, self.chkbox_Checkbox2_XPATH).click()
        elif chkbx == "chk3":
            self.driver.find_element(By.XPATH, self.chkbox_Checkbox3_XPATH).click()
        elif chkbx == "chk4":
            self.driver.find_element(By.XPATH, self.chkbox_Checkbox4_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.chkbox_Checkbox1_XPATH).click()

    def setText(self, txt):
        self.driver.find_element(By.XPATH, self.txtbox_text_XPATH).clear()
        self.driver.find_element(By.XPATH, self.txtbox_text_XPATH).send_keys(txt)

    def selectColor(self,color):
        drpdown = Select(self.driver.find_element(By.XPATH, self.drpdown_SelectColor_XPATH))
        drpdown.select_by_value(color)

    def setTextArea(self, txt):
        self.driver.find_element(By.XPATH, self.txtbox_textArea_XPATH).clear()
        self.driver.find_element(By.XPATH, self.txtbox_textArea_XPATH).send_keys(txt)

    def setdate(self,date):
        # self.driver.find_element(By.XPATH, self.txtbox_textArea_XPATH).click()
        # next = self.driver.find_element(By.XPATH, self.button_Next_XPATH)
        # monthyear = self.driver.find_element(By.XPATH, self.thMonthyear_XPATH)
        # while monthyear.text != "April 2022":
        #     next.click()
        # day = self.driver.find_element(By.XPATH, self.button_Day_XPATH)
        # day.click()
        self.driver.find_element(By.XPATH, self.inputDate_XPATH).clear()
        self.driver.find_element(By.XPATH, self.inputDate_XPATH).send_keys(date)



















