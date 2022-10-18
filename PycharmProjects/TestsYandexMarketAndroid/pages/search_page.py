from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class Locators:
    SEARCH_FIELD_ON_MAIN_PAGE = (By.ID, 'ru.beru.android:id/searchRequestView')
    SEARCH_FIELD_AFTER_CLICK = (By.ID, 'ru.beru.android:id/viewSearchAppBarLayoutInput')
    SEARCH_BUTTON = (By.ID, 'ru.beru.android:id/viewSearchAppBarLayoutSearchIcon')
    PRODUCT_CARD = (By.ID, 'ru.beru.android:id/description')


class SearchPage(BasePage):
    def __init__(self, driver):
        self._driver = driver

    def click_on_search_field(self):
        self.find_element(Locators.SEARCH_FIELD_ON_MAIN_PAGE).click()

    def write_playstation5(self):
        self.find_element(Locators.SEARCH_FIELD_AFTER_CLICK).send_keys(
            'Playstation 5')

    def click_on_search_button(self):
        self.find_element(Locators.SEARCH_BUTTON).click()

    def wait_on_element_text(self):
        WebDriverWait(self._driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'ru.beru.android:id/description'), 'Playstation 5')
        )

    def click_on_the_product_card(self):
        self.find_element(Locators.PRODUCT_CARD).click()

    def swipe_element(self):
        self._driver.swipe(980, 700, 100, 750, 500)
        self._driver.swipe(980, 700, 100, 750, 500)
        self._driver.swipe(980, 700, 100, 750, 500)
        self._driver.swipe(100, 750, 980, 700, 500)
        self._driver.swipe(100, 750, 980, 700, 500)
