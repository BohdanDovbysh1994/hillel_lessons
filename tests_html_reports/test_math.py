import pytest
from pytest_html_reporter import attach


def test_sum():
    assert 2 + 2 == 4, 'Not as expected'


def test_sum_failed():
    assert 2 + 2 == 7, 'Not as expected'


@pytest.mark.skip('TEST SKIP BLA')
def test_skip():
    assert 2 + 2 == 7, 'Not as expected'


def test_error():
    raise Exception('TESTS')


def test_screenshot():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://pypi.org/project/webdriver-manager/')
    attach(data=driver.get_screenshot_as_png())
    driver.quit()
