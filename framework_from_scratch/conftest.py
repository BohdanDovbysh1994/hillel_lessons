from telnetlib import EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from framework_from_scratch.page_objects.home_page import HomePage
from framework_from_scratch.utilities.driver_factory import DriverFactory


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1, is_headless=False)
    driver.get('http://automationpractice.com/index.php')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def get_home_page(create_driver):
    return HomePage(create_driver)
