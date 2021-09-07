from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FIRST_PRODUCT_IN_BASKET)

    def should_be_message_empty_basket(self):
        msg = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MSG)
        assert 'empty' in msg.text
