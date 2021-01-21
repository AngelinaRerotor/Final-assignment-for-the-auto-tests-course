from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_busket(self):
        busket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        busket.click()

    def should_be_to_basket(self):
        self.matching_name()
        self.matching_price()

    def matching_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET).text
        assert product_name == message_name, f"{product_name} is not {message_name}"

    def matching_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_CART_PRICE).text
        assert product_price == message_price, f"{product_price} not equal {message_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_disapper_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message persists"
