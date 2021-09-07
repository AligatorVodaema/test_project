from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
            'substring login not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is not presented'

    def register_new_user(self, email: str, password: str):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FIELD_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_FIELD_PASSWORD1
        )
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_FIELD_PASSWORD2
        )
        confirm_password_field.send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON
        ).click()
