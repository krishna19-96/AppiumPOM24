from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class ScrollUtil:
    @staticmethod
    def scrollToTextByAndroidUiAutomator(text,driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiScrollable(new UiSelector().scrollable("
                                                         "true).instance(0)).scrollIntoView(new UiSelector("
                                                         ").textContains(\"" + text + "\").instance(0))").click()
        # driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(
        # 0)).scrollIntoView(new UiSelector().textContains(\"" + text + "\").instance(0))").click()

    @staticmethod
    def swipeUp(noofswipes, driver):
        for i in range(1,noofswipes+1):
            device_size = driver.get_window_size()
            # print(device_size)
            screenWidth = device_size['width']
            screenHeight = device_size['height']
            # print(screenWidth)
            # print(screenHeight)
            # it's an mathematical operation
            startX = screenWidth / 2
            endX = screenWidth / 2
            startY = screenHeight * 8 / 9
            endY = screenHeight / 9
            # print(startX)
            # print(endX)
            # print(startY)
            # print(endY)
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(startX, startY)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(2)
            actions.w3c_actions.pointer_action.move_to_location(endX, endY)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            # actions.click()

    @staticmethod
    def swipeDown(noofswipes, driver):
        for i in range(1,noofswipes + 1):
            device_size = driver.get_window_size()
            # print(device_size)
            screenWidth = device_size['width']
            screenHeight = device_size['height']
            # print(screenWidth)
            # print(screenHeight)
            # it's an mathematical operation
            startX = screenWidth / 2
            endX = screenWidth / 2
            startY = screenHeight * 8 / 9
            endY = screenHeight / 9
            # print(startX)
            # print(endX)
            # print(startY)
            # print(endY)
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(endX, endY)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(2)
            actions.w3c_actions.pointer_action.move_to_location(startX, startY)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            # actions.click()

