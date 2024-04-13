from Pages.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest
import pytest
from Utilities import excelReader
from Pages.OpenTruck import OpenTruck

class Test_LoginPage(BaseTest):

    @pytest.mark.parametrize("Area,Name", excelReader.getAllCellData("Area"))
    def test_searchtruck(self, Area, Name):
        home = HomeScreen(self.driver)
        Truck = home.goto_Open_Truck().searchTruck(Area, Name)
        print("Truck",  Truck)
        Vehicle_Type, Vehicle_Price = Truck
        assert "Tata Ace Closed" == Vehicle_Type
        print("Vehicle_Price", Vehicle_Price)