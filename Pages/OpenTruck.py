from Pages.BasePage import BasePage


class OpenTruck(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def searchTruck(self, Area, Name):
        self.click("localTruck_ID")
        self.type("DropLocation_ID", Area)
        self.click("DropLocationsuggestion1_XPATH")
        self.type("ReceiverName_ID", Name)
        self.click("Usemymobilenumbercheckbox_ID")
        self.click("Saveoption_ID")
        self.click("Confirmbtn_ID")
        Vehicle_Type = self.getText("Vehicletype_ID")
        Vehile_Price = self.getText("Vehicleprice_ID")
        return Vehicle_Type, Vehile_Price

