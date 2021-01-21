from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        login_url = self.browser.current_url
        assert "login" in login_url, "URL does not contain 'login'"

    def should_be_login_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "fakepassword"
        input_email_address = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS).send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()
