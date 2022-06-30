import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Bohdan Dovbysh')
@allure.feature('https://docs.qameta.io/allure/#_pytest')
def test_home_page_phone_number(get_home_page):
    home_page = get_home_page
    actual_number = home_page.get_current_phone_number()
    assert actual_number == '0123-456-789', \
        f'\nNumber not as expected\nActual: {actual_number}\nExpected: "0123-456-789"'


@allure.feature('Bohdan Dovbysh')
@allure.feature('https://docs.qameta.io/allure/#_pytest')
@pytest.mark.please_run_first
def test_login_to_app(get_home_page):
    """
    STEPS:
    1. STEP_1
    2. STEP_@
    EXPECTED:
    EXPECTED_1
    EXPECTED_2
    """
    with allure.step('STep_1'):
        user_email = 'dovbysh.bohdan@gmail.com'
        user_password = 'bohdan'
        home_page = get_home_page
        login_page = home_page.click_sign_in()
        # user_page = login_page.set_user_email(user_email).set_password(user_password).click_login_button()
        user_page = login_page.login(user_email, user_password)
        assert user_page.title == 'My account - My Store', \
            f'\nUser not logined\nActual title: {user_page.title}, Expected: \'My account - My store\''
    with allure.step('STEP_2'):
        assert 1 == 3, 'EXPECTED_2'

@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False


@allure.issue('https://pypi.org/project/pytest-html/', 'Known issue')
def test_skip():
    pass


# def test_modal(create_driver):
#     driver = create_driver
#     # driver.implicitly_wait(15)
#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-popup]/span")))
#     # element = driver.find_element(By.XPATH, "//span[text() = 'Вхід']")
#     element.click()
#
#     modal_locator = "//div[@id='popup-auth']"
#     login_element = '//input[@name="user_login"]'
#     element_modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, login_element)))
#     element_modal.click()
#     element_modal.send_keys('TESTS')
#     c = 0
