import logging

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import configReader
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.Wait = WebDriverWait(driver,20)

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            #Xpath
            self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).click()
        log.logger.info("Clicking on an Element " + str(locator))


    def clicks(self, locator, Index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements(AppiumBy.XPATH, configReader.readConfig("locators", locator)[Index]).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID,
                                      configReader.readConfig("locators", locator)[Index]).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements(AppiumBy.ID, configReader.readConfig("locators", locator)[Index]).click()
        log.logger.info("Clicking on an Element" + str(locator) + "Index is" + str(Index))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Clicking on an Element" + str(locator + "Entered the value is" + str(value)))

    def getText(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                            configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).text
        log.logger.info("Clicking on an Element" + str(locator))
        return text

    # def alert(self):
    #     self.driver._switch_to.alert().accept()