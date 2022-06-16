import pytest

from framework_from_scratch.page_objects.home_page.home_page import HomePage
from framework_from_scratch.utilities.driver_factory import DriverFactory
from framework_from_scratch.utilities.read_run_settings import ReadConfig


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id(),
                                         is_headless=ReadConfig.get_headless_mod())
    driver.get(ReadConfig.get_application_url())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def get_home_page(create_driver):
    return HomePage('STRING')
