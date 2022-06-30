from contextlib import suppress

import allure
import pytest

from framework_from_scratch.page_objects.home_page.home_page import HomePage
from framework_from_scratch.utilities.driver_factory import DriverFactory
from framework_from_scratch.utilities.read_run_settings import ReadConfig


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def create_driver(request):
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id(),
                                         is_headless=ReadConfig.get_headless_mod())
    driver.get('http://automationpractice.com/index.php')
    driver.maximize_window()
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture
def get_home_page(create_driver):
    return HomePage(create_driver)
