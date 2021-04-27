from selenium import webdriver
from selenium.webdriver.support.select import Select
class Base:
    def browser_launch(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\Users\Mirdula K\PycharmProjects\Frameworks-Utility\Framework - Page Object Model (POM) - Adactin(Example)\Drivers\chromedriver.exe")
        return self.driver
    def maximize(self):
        self.driver.maximize_window()
    def load_url(self,url):
        self.driver.get(url)
    def fill(self,e,data):
        e.send_keys(data)
    def dd_by_visible_text(self,e,text):
        s=Select(e)
        s.select_by_visible_text(text)
    def dd_by_value(self,e,value):
        s=Select(e)
        s.select_by_value(value)
    def dd_by_index(self,e,index):
        s=Select(e)
        s.select_by_index(index)
    def btn_click(selfm,element):
        element.click()
    def attribute(self,e):
        r=e.get_attribute("value")
        return r
