from selenium.webdriver.common.by import By

from framework_from_scratch.utilities.web_ui.locators import Locator


class HomePageLocators:

    def __init__(self):
        self.__phone_number_label = Locator(By.XPATH, "//span[@class='shop-phone']/strong")
        self.__sign_in_button = Locator(By.CSS_SELECTOR, '.header_user_info')

    @property
    def phone_number_label(self):
        return self.__phone_number_label.get_locator()

    @property
    def sign_in_button(self):
        return self.__sign_in_button.get_locator()
