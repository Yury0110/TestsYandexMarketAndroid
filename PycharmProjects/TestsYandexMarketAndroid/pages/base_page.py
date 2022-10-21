from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Locators:
    ACCEPT_LOCATION_BANNER = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                        ".widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                                        "/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
                                        ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                        ".view.ViewGroup/android.widget.Button[2]")
    CLOSE_AD_BANNER = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                 '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                 '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                                 '.ImageButton')
    SKIP_COOKIE_BANNER = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                    '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                    '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                    '/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button['
                                    '1]')


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def wait_on_element_text(self, locator, text):
        WebDriverWait(self._driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, locator), text)
        )

    def close_banners(self):
        self.find_element(Locators.CLOSE_AD_BANNER).click()
        self.find_element(Locators.ACCEPT_LOCATION_BANNER).click()
        self.find_element(Locators.SKIP_COOKIE_BANNER).click()
