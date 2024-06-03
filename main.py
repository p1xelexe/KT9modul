import time
import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_shorts(self) -> None:
        self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                 value='new UiSelector().resourceId("com.google.android.youtube:id/image").instance(2)').click()

    def test_tap(self) -> None:
        self.driver.tap([(399, 2072)])

    def test_scroll(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().className("android.widget.ImageView").instance(4)')
        el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().className("android.widget.ImageView").instance(5)')
        self.driver.scroll(el1, el2)

    def test_swipe(self) -> None:
        self.driver.tap([(505, 725)])
        time.sleep(2)
        self.driver.swipe(32, 356, 346, 356)
        time.sleep(10)

    def test_home(self) -> None:
        self.driver.find_element(by=AppiumBy.ID,
                                 value='new UiSelector().resourceId("android:id/navigationBarBackground")').click()

    # --------------------------------------------------------

    def test_search(self):
        search_element = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                  value='new UiSelector().description("Search")')

        search_element.click()

    def test_text(self):
        search_box = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.youtube:id/search_edit_text')

        search_box.send_keys('test')

        search_button = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                 value='new UiSelector().className("android.view.ViewGroup").instance(5)')

        search_button.click()

    def test_filters(self):
        search_element = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                  value='new UiSelector().description("More options")')
        search_element.click()
        time.sleep(3)
        search_element2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                   value='new UiSelector().text("Search filters")')
        search_element2.click()
        time.sleep(3)
        filters = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Live")')
        filters.click()
        time.sleep(3)
        apply = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                         value='new UiSelector().resourceId("com.google.android.youtube:id/apply")')
        apply.click()

    def test_action_menu(self):

        search_element = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                  value='new UiSelector().description("Action menu").instance(0)')
        search_element.click()
        time.sleep(3)
        next = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                        value='new UiSelector().text("Play next in queue")')
        next.click()

    def test_back(self):
        back = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                        value='new UiSelector().description("Navigate up")')
        back.click()
