from selenium.webdriver.common.by import By
from POM import Locators


class HotelSearch:
    def __init__(self,driver):
        self.locationId=driver.find_element(By.ID,Locators.location_id)
        self.hotelId=driver.find_element(By.ID,Locators.hotels_id)
        self.roomTypes=driver.find_element(By.ID,Locators.roomType_id)
        self.roomNos=driver.find_element(By.ID,Locators.roomNos_id)
        # self.checKIn=driver.find_element(By.ID,Locators.checkIn_id)
        # self.checkOut=driver.find_element(By.ID,Locators.checkOut_id)
        self.adultsCountNo=driver.find_element(By.ID,Locators.adultsCount_id)
        self.childCountNo=driver.find_element(By.ID,Locators.childCount_id)
        self.btnSearch=driver.find_element(By.ID,Locators.btnSearch_id)


    def getLocate(self):
        return self.locationId
    def getHotel(self):
        return self.hotelId
    def getRoomTypes(self):
        return self.roomTypes
    def getRoomNos(self):
        return self.roomNos
    # def getCheckIn(self):
    #     return self.checKIn
    # def getCheckOut(self):
    #     return self.checkOut
    def getadults(self):
        return self.adultsCountNo
    def getChild(self):
        return self.childCountNo
    def getbtnSearchBox(self):
        return self.btnSearch

