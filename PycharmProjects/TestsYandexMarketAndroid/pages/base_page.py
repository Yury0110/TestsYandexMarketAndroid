from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Locators:
    CLOSE_AD_BANNER = (By.ID, "ru.beru.android:id/closeButton")
    ACCEPT_LOCATION_BANNER = (By.ID, 'ru.beru.android:id/agreeButton')
    SKIP_COOKIE_BANNER = (By.ID, "ru.beru.android:id/negativeButton")


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def close_banners(self):
        self.find_element(Locators.CLOSE_AD_BANNER).click()
        self.find_element(Locators.ACCEPT_LOCATION_BANNER).click()
        self.find_element(Locators.SKIP_COOKIE_BANNER).click()
