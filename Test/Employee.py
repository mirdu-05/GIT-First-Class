import time

from selenium import webdriver
from libGlobal.LibGlobal import Base
from POM.Adactin.LoginPage_1 import LoginPage
from POM.Adactin.HotelSearch_2 import HotelSearch
from POM.Adactin.SelectHotel_3 import SelectHotel
from POM.Adactin.BookAHotel_4 import Book_Hotel
from POM.Adactin.BookingConfirmation_5 import BookingConfirmation


class emp(Base):
    def login(self):
        driver=self.browser_launch()
        self.maximize()
        self.load_url("https://adactinhotelapp.com/")

        #Login Page 1
        l=LoginPage(driver)
        self.fill(l.getTxtUserName(),"MirdulaAditi")
        self.fill(l.getTxtPwd(),"NJG167")
        self.btn_click(l.getBtnLogin())

        #Hotel search 2

        h=HotelSearch(driver)
        self.btn_click(h.getLocate())
        self.dd_by_visible_text(h.getLocate(),"Brisbane")
        self.btn_click(h.getHotel())
        self.dd_by_visible_text(h.getHotel(),"Hotel Creek")
        self.btn_click(h.getRoomTypes())
        self.dd_by_index(h.getRoomTypes(),1)
        self.btn_click(h.getRoomNos())
        self.dd_by_value(h.getRoomNos(),"4")
        self.btn_click(h.getadults())
        self.dd_by_visible_text(h.getadults(),"4 - Four")
        self.btn_click(h.getChild())
        self.dd_by_index(h.getChild(),2)
        self.btn_click(h.getbtnSearchBox())

        #Select Hotel 3

        s=SelectHotel(driver)
        self.btn_click(s.getRadioBtn())
        self.btn_click(s.getBtnContinue())

        #Book A Hotel 4

        b=Book_Hotel(driver)
        self.fill(b.getFName(),"Mirdula")
        self.fill(b.getLName(),"K")
        self.fill(b.getBillAddress(),"NO 298, 3rd main road, Anna Nagar,Chennai-40")
        self.fill(b.getCcard(),"0975636352164286")
        self.btn_click(b.getCardType())
        self.dd_by_visible_text(b.getCardType(),"VISA")
        self.btn_click(b.getCexpMon())
        self.dd_by_visible_text(b.getCexpMon(),"July")
        self.btn_click(b.getcExpYr())
        self.dd_by_value(b.getcExpYr(),"2022")
        self.fill(b.getCardCVV(),"876")
        self.btn_click(b.getBtnBook())
        time.sleep(8)

        #Booking Confirmation 5
        t = BookingConfirmation(driver)
        att = self.attribute(t.orderNo)
        print(att)


m=emp()
m.login()


