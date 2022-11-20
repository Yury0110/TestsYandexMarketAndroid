from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import time


class Locators:
    SEARCH_FIELD_ON_MAIN_PAGE = (By.XPATH, '//android.view.ViewGroup[@content-desc="Поиск товаров"]')

    SEARCH_FIELD_AFTER_CLICK = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                          '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                          '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                          '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                          '.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup'
                                          '/android.widget.FrameLayout/android.widget.EditText')

    SEARCH_BUTTON = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.LinearLayout/android.view.ViewGroup/android.widget.ImageView[2]')

    SORT_BUTTON = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                             '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                             '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.ScrollView/android.widget.LinearLayout/android.view.ViewGroup['
                             '2]/android.widget.Spinner/android.widget.TextView')

    DISCOUNT_BUTTON = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                 '.ListView/android.widget.TextView[5]')

    CLOSE_PRODUCT_CARD = (By.XPATH,
                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                          '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
                          '/android.widget.ImageButton')

    ITEM_1 = (By.XPATH, '(//android.widget.FrameLayout[@content-desc="В корзину"])['
                        '4]/android.widget.FrameLayout')

    ITEM_2 = (By.XPATH, '(//android.widget.FrameLayout[@content-desc="В корзину"])['
                        '5]/android.widget.FrameLayout')

    REMOVE_ITEM = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                             '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                             '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget'
                             '.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                             '.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                             '/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.ImageButton')

    CARD = (By.ID, 'ru.beru.android:id/nav_cart')

    PRODUCT_CARD = (By.ID, 'ru.beru.android:id/productContainer')


class SearchPage(BasePage):
    def __init__(self, driver):
        self._driver = driver

    def click_on_search_field(self):
        self.find_element(Locators.SEARCH_FIELD_ON_MAIN_PAGE).click()

    def write_playstation5(self):
        self.find_element(Locators.SEARCH_FIELD_AFTER_CLICK).send_keys('Playstation 5')

    def click_on_search_button(self):
        self.find_element(Locators.SEARCH_BUTTON).click()

    def swipe_element(self):
        self._driver.swipe(980, 700, 100, 750, 500)
        self._driver.swipe(980, 700, 100, 750, 500)
        self._driver.swipe(980, 700, 100, 750, 500)
        self._driver.swipe(100, 750, 980, 700, 500)
        self._driver.swipe(100, 750, 980, 700, 500)

    def add_items_to_card(self):
        self.find_element(Locators.PRODUCT_CARD).is_displayed()

        self._driver.swipe(500, 1450, 540, 660, 700)

        self.find_element(Locators.ITEM_1).click()
        self.find_element(Locators.ITEM_2).click()

    def go_to_card(self):

        self.find_element(Locators.CARD).click()

        self._driver.swipe(550, 990, 540, 670, 700)

    def remove_items_from_card(self):
        self.find_element(Locators.REMOVE_ITEM).click()
        self.find_element(Locators.REMOVE_ITEM).click()

    def click_on_the_product_card(self):
        self.find_element(Locators.PRODUCT_CARD).click()
