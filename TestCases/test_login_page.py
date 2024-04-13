from Pages.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest
import pytest
from Utilities import excelReader


class Test_LoginPage(BaseTest):

    @pytest.mark.parametrize("MobileNumber", excelReader.getAllCellData("MobileNumber"))
    def test_loginpage(self, MobileNumber):
        home = HomeScreen(self.driver)
        home.gotoLoginPage().loginPage(MobileNumber)