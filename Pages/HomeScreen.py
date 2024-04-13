from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.OpenTruck import OpenTruck


class HomeScreen(BasePage):

    def __init__(self, driver):
        """

        :rtype: object
        """
        super().__init__(driver)

    def goto_Open_Truck(self):
        self.click("Truck_XPATH")
        return OpenTruck(self.driver)

    def gotoLoginPage(self):
        print("Login page")
        return LoginPage(self.driver)

