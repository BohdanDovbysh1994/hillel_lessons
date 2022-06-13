from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework_from_scratch.page_objects.login_page import LoginPage
from framework_from_scratch.utilities.web_ui.base_page import BasePage


class HomePage(BasePage):
    __phone_number_label = (By.XPATH, "//span[@class='shop-phone']/strong")
    __sign_in_button = (By.CSS_SELECTOR, '.header_user_info')

    def __init__(self, driver):
        super().__init__(driver)

    def get_current_phone_number(self):
        phone_number_element = self.wait_until_element_located(self.__phone_number_label)
        return self.get_text(phone_number_element)

    def click_sign_in(self):
        self.click(self.__sign_in_button)
        return LoginPage(self._driver)

