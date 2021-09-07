from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOP_CART = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FIELD_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FIELD_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FIELD_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value='Register']")


class ProductPageLocators:
    # ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[value='Add to basket']")
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    ADD_MSG_TO_CART = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.XPATH, "//strong [contains(text(), 'Coders at Work')]")


class BasketPageLocators:
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, '#content_inner p')
    FIRST_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
