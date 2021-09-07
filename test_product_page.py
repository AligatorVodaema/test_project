import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import faker
import random
from links import PROMO_LINKS


@pytest.mark.need_review
@pytest.mark.parametrize('link', PROMO_LINKS)
@pytest.mark.xfail(reason='one of ten links dont have message about add product')
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.should_be_product_page()
    product_title = product_page.get_title_of_product().text

    product_page.guest_can_add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    add_message = product_page.get_add_message().text
    product_page.should_be_same_title(product_title, add_message)


@pytest.mark.xfail(reason='should be success message')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, url=link, timeout=0)
    product_page.open()
    product_page.guest_can_add_item_to_cart()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason='should be success message')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, url=link, timeout=0)
    product_page.open()
    product_page.guest_can_add_item_to_cart()
    product_page.should_not_be_disappeared_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    main_page = ProductPage(browser, url=link)
    main_page.open()
    main_page.go_to_shop_cart()
    basket_page = BasketPage(browser, url=browser.current_url, timeout=0)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_message_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        register_url = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        register_page = LoginPage(browser, url=register_url)
        register_page.open()
        random_email = faker.Faker().email()
        random_pass = str(random.randint(100000000, 1000000000))
        register_page.register_new_user(random_email, random_pass)
        register_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, url=link, timeout=0)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        product_page.should_be_product_page()
        product_title = product_page.get_title_of_product().text

        product_page.guest_can_add_item_to_cart()
        product_page.solve_quiz_and_get_code()
        add_message = product_page.get_add_message().text
        product_page.should_be_same_title(product_title, add_message)
