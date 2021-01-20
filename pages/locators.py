from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div h1")
    PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    MESSAGE_CART_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
