from selenium.webdriver.common.by import By
from POM import Locators

class Book_Hotel:
    def __init__(self,driver):
        self.firstName=driver.find_element(By.ID,Locators.fname_id)
        self.lastname=driver.find_element(By.ID,Locators.lname_id)
        self.billAddress=driver.find_element(By.ID,Locators.address_id)
        self.cCard=driver.find_element(By.ID,Locators.creditCard_id)
        self.cCardType=driver.find_element(By.ID,Locators.cardType_id)
        self.cCardExpMon=driver.find_element(By.ID,Locators.cardExpMonth_id)
        self.cCardExpYr=driver.find_element(By.ID,Locators.cardExpYear_id)
        self.cCardCVV=driver.find_element(By.ID,Locators.cardCvvNo_id)
        self.btnBookNow=driver.find_element(By.ID,Locators.btnBookNow_id)

    def getFName(self):
        return self.firstName
    def getLName(self):
        return self.lastname
    def getBillAddress(self):
        return self.billAddress
    def getCcard(self):
        return self.cCard
    def getCardType(self):
        return self.cCardType
    def getCexpMon(self):
        return self.cCardExpMon
    def getcExpYr(self):
        return self.cCardExpYr
    def getCardCVV(self):
        return self.cCardCVV
    def getBtnBook(self):
        return self.btnBookNow
