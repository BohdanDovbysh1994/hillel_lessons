import time
from time import sleep

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys



def test_01():
    driver_chrome = Chrome("chromedriver.exe")
    driver_chrome.maximize_window()
    driver_chrome.get('http://admin-demo.nopcommerce.com')
    our_title = driver_chrome.title
    assert our_title == 'Your store. Login!!!!', f'\nWrong title\nActual: {our_title}\nExpected: "Your store. Login"'


def test_02():
    user_email = 'admin@yourstore.com'
    user_password = 'admin'
    driver_chrome = Chrome("chromedriver.exe")
    driver_chrome.maximize_window()
    driver_chrome.get('http://admin-demo.nopcommerce.com')
    email_input_locator = "//input[@class='email valid']"
    time.sleep(3)
    email_input_element = driver_chrome.find_element(By.XPATH, email_input_locator)
    email_input_element.clear()
    email_input_element.send_keys(user_email)
    driver_chrome.save_screenshot('our_screenshot.jpg')
    time.sleep(3)
    password_input_id = 'Password'
    password_input_element = driver_chrome.find_element(By.ID, password_input_id)
    password_input_element.clear()
    password_input_element.send_keys(user_password)
    time.sleep(3)
    login_btn_css_locator = 'button'
    login_button_element = driver_chrome.find_element(By.CSS_SELECTOR, login_btn_css_locator)
    login_button_element.click()
    time.sleep(5)
    current_title = driver_chrome.title
    driver_chrome.quit()
    assert current_title == 'Dashboard / nopCommerce administration', \
        f'\nActual: {current_title}\nExpected: "EXPECTED"'


def test_action_chain():
    user_email = 'admin@yourstore.com'
    user_password = 'admin'
    driver_chrome = Chrome("chromedriver.exe")
    driver_chrome.maximize_window()
    driver_chrome.get('http://admin-demo.nopcommerce.com')
    actions = ActionChains(driver_chrome)
    email_input_locator = "//input[@class='email valid']"
    email_input_element = driver_chrome.find_element(By.XPATH, email_input_locator)
    password_input_id = 'Password'
    password_input_element = driver_chrome.find_element(By.ID, password_input_id)
    login_btn_css_locator = 'button'
    login_button_element = driver_chrome.find_element(By.CSS_SELECTOR, login_btn_css_locator)
    actions.double_click(login_button_element).perform()

    driver_chrome.switch_to.alert.dismiss()

    driver_chrome.command_executor('print(BLABLA)')


