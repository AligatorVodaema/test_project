from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#Qlogin_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#Qregister_form')


class ProductPageLocators:
    # ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[value='Add to basket']")
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    ADD_MSG_TO_CART = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.XPATH, "//strong [contains(text(), 'Coders at Work')]")
