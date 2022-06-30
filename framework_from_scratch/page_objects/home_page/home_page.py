from allure_commons.types import AttachmentType

from framework_from_scratch.page_objects.home_page.home_page_locators import HomePageLocators
from framework_from_scratch.page_objects.login_page import LoginPage
from framework_from_scratch.utilities.web_ui.base_page import BasePage
import allure


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__home_page_elements = HomePageLocators()

    @allure.step
    def get_current_phone_number(self):
        phone_number_element = self.wait_until_element_located(self.__home_page_elements.phone_number_label)
        return self.get_text(phone_number_element)

    @allure.step
    def click_sign_in(self):
        self.click(self.__home_page_elements.sign_in_button)
        return LoginPage(self._driver)
