from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.CSS_SELECTOR, "span[class='btn-group'] a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.ID, "basket_formset")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, ".content > div#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_ADDRESS = (By.ID, "id_registration-email")
    PASSWORD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    BUTTON_REGISTER = (By.NAME, "registration_submit")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div h1")
    PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    MESSAGE_CART_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")




