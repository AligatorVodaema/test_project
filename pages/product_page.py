from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_item_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    def get_title_of_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)

    def get_add_message(self):
        return self.browser.find_element(*ProductPageLocators.ADD_MSG_TO_CART)

    def should_be_product_page(self):
        self.should_be_title_of_product()
        self.should_be_price_of_product()
        self.should_be_add_button_to_cart()

    def should_be_add_button_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON)

    def should_be_title_of_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE)

    def should_be_price_of_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be."

    def should_not_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should not be."
