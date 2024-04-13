import time

from Pages.BasePage import BasePage
from Pages import HomeScreen


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def loginPage(self, MobileNumber):
        # time.sleep(3)
        self.click("LocationPermission_XPATH")
        time.sleep(3)
        self.click("NotificationPermission_ID")
        for lis in MobileNumber:
            self.type("MobileNumber_ID", lis)
        self.click("MobileNumber_ID")
        self.click("Login_ID")
        # return HomeScreen.OpenTruck(self.driver)


