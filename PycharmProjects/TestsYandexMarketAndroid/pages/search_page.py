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

    PRODUCT_CARD_1 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/androidx'
                                '.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                '1]/android.widget.LinearLayout/android.widget.TextView')

    PRODUCT_CARD_2 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                      '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android'
                      '.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                      '.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.FrameLayout'
                      '/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                      '2]/android.widget.LinearLayout/android.widget.TextView')

    PRODUCT_CARD_3 = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                      '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android'
                      '.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                      '.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.FrameLayout'
                      '/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                      '3]/android.widget.LinearLayout/android.widget.TextView')

    DISCOUNT_LABEL = (By.XPATH, '//androidx.recyclerview.widget.RecyclerView['
                                '@content-desc="product_root_recycler"]/android.widget.LinearLayout/android.view'
                                '.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout['
                                '1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView')


class SearchPage(BasePage):
    def __init__(self, driver):
        self._driver = driver

    def click_on_search_field(self):
        self.find_element(Locators.SEARCH_FIELD_ON_MAIN_PAGE).click()

    def write_playstation5(self):
        self.find_element(Locators.SEARCH_FIELD_AFTER_CLICK).send_keys('Playstation 5')

    def click_on_search_button(self):
        self.find_element(Locators.SEARCH_BUTTON).click()

    def click_on_the_product_card(self):
        self.find_element(Locators.PRODUCT_CARD_1).click()

    def swipe_element(self):
        self._driver.swipe(980, 700, 100, 750, 500)
        self._driver.swipe(980, 700, 100, 750, 500)
        self._driver.swipe(980, 700, 100, 750, 500)
        self._driver.swipe(100, 750, 980, 700, 500)
        self._driver.swipe(100, 750, 980, 700, 500)

    def sort_items_by_discount_and_approve(self):
        self.find_element(Locators.SORT_BUTTON).click()
        self.find_element(Locators.DISCOUNT_BUTTON).click()
        self.find_element(Locators.PRODUCT_CARD_1).click()

        # get discount of 1st element
        a = self.find_element(Locators.DISCOUNT_LABEL).get_attribute('text')
        str1 = str(a.replace(' ', '').replace('%', ''))
        self.find_element(Locators.CLOSE_PRODUCT_CARD).click()

        # get discount of 2st element
        self.find_element(Locators.PRODUCT_CARD_2).click()
        b = self.find_element(Locators.DISCOUNT_LABEL).get_attribute('text')
        str2 = str(b.replace(' ', '').replace('%', ''))
        self.find_element(Locators.CLOSE_PRODUCT_CARD).click()

        # get discount of 3st element
        self.find_element(Locators.PRODUCT_CARD_3).click()
        c = self.find_element(Locators.DISCOUNT_LABEL).get_attribute('text')
        str3 = str(c.replace(' ', '').replace('%', ''))
        self.find_element(Locators.CLOSE_PRODUCT_CARD).click()

        if str1 > str2 and str2 > str3:
            return True
        else:
            return False
