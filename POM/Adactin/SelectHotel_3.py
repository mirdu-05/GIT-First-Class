from selenium.webdriver.common.by import By
from POM import Locators

class SelectHotel:
    def __init__(self,driver):
        self.radioBtn1=driver.find_element(By.ID,Locators.radioBtn_id)
        self.btnContinue1=driver.find_element(By.ID,Locators.btnContinue_id)

    def getRadioBtn(self):
        return self.radioBtn1
    def getBtnContinue(self):
        return self.btnContinue1



