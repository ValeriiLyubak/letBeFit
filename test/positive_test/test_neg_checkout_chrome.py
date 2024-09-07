from browser_factory.browser_factory import BrowserFactory
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage
from pages.order_confirm_page import OrderConfirmPage


def test_neg_checkout_chrome():
    browser = "chrome"
    driver = BrowserFactory(browser).get_driver()

    print("Начинаем позитивный тест по оформлению заказа на Chrome")

    try:
        main_page = MainPage(driver)
        main_page.landing_page()
        main_page.input_phone_field("9085543490")
        main_page.click_order_button()
        checkout_page = CheckoutPage(driver)
        checkout_page.click_confirm_button()
        actual_message = checkout_page.get_empty_name_field_message()
        expected_message = "Поле обязательно к заполнению"
        assert expected_message == actual_message, f"Ожидалось '{expected_message}', но получили '{actual_message}'"
        actual_message = checkout_page.get_empty_email_field_message()
        expected_message = "Введите корректный email"
        assert expected_message == actual_message, f"Ожидалось '{expected_message}', но получили '{actual_message}'"
    finally:
        driver.quit()
        print("тест успешно пройден")


test_neg_checkout_chrome()