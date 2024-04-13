import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    desired_caps = dict(
        platformName='Android',
        deviceName='LMF100EMW618825c3',
        appPackage='com.theporter.android.customerapp',
        appActivity='com.theporter.android.customerapp.RootActivity',
        udid='LMF100EMW618825c3',
        automationName ='uiAutomator2',
        appWaitDuration="590000",
        noReset=True
    )
    # appium_url = 'http://127.0.0.1:4723'
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    # driver = webdriver.Remote(appium_url, options=AppiumOptions().load_capabilities(desired_caps))
    # print("Current session is 1 {}".format(driver.session_id))
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Failure", attachment_type=AttachmentType.PNG)






