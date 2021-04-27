from selenium.webdriver.common.by import By
from POM import Locators
class BookingConfirmation:
    def __init__(self,driver):
        self.orderNo=driver.find_element(By.ID,Locators.bookingId_id)


    def getorderNo(self):
        return self.orderNo
