def test_home_page_phone_number(get_home_page):
    home_page = get_home_page
    actual_number = home_page.get_current_phone_number()
    assert actual_number == '0123-456-789', \
        f'\nNumber not as expected\nActual: {actual_number}\nExpected: "0123-456-789"'


def test_login_to_app(get_home_page):
    user_email = 'dovbysh.bohdan@gmail.com'
    user_password = 'bohdan'
    home_page = get_home_page
    login_page = home_page.click_sign_in()
    user_page = login_page.set_user_email(user_email).set_password(user_password).click_login_button()
    assert user_page.title == 'My account - My Store', \
        f'\nUser not logined\nActual title: {user_page.title}, Expected: \'My account - My store\''
