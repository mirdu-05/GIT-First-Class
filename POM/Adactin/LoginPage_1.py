from selenium.webdriver.common.by import By
from POM import Locators

class LoginPage:
    def __init__(self,driver):
        self.txt_username=driver.find_element(By.ID,Locators.userName_id)
        self.txt_pwd=driver.find_element(By.ID,Locators.pwd_id)
        self.btn_Login=driver.find_element(By.XPATH,Locators.btn_login_Xpath)

    def getTxtUserName(self):
        return self.txt_username
    def getTxtPwd(self):
        return self.txt_pwd
    def getBtnLogin(self):
        return self.btn_Login
