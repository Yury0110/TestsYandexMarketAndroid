from pages.search_page import BasePage
from pages.search_page import SearchPage
from selenium.webdriver.common.by import By
import time


class TestSearch:
    def test_add_product_in_card_and_delete_from_card(self, mobile_driver):
        """
        test of add and remove items from card
        """
        close = BasePage(mobile_driver)
        close.close_banners()
        search = SearchPage(mobile_driver)
        search.click_on_search_field()
        search.write_playstation5()
        search.click_on_search_button()
        search.add_items_to_card()
        search.go_to_card()
        search.remove_items_from_card()


class TestSwipe:
    def test_swipe_images_in_product_card(self, mobile_driver):
        """
        test of swiping images in product card
        """
        close = BasePage(mobile_driver)
        close.close_banners()
        swipe = SearchPage(mobile_driver)
        swipe.click_on_search_field()
        swipe.write_playstation5()
        swipe.click_on_search_button()
        swipe.click_on_the_product_card()
        swipe.swipe_element()

