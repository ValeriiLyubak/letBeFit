import time

from browser_factory.browser_factory import BrowserFactory
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage


def test_neg_checkout_firefox():
    browser = "firefox"
    driver = BrowserFactory(browser).get_driver()

    print("Начинаем тест негативного сценария без ввода имени и email на Firefox")

    try:
        main_page = MainPage(driver)
        main_page.landing_page()
        time.sleep(2)
        main_page.input_phone_field("9085543490")
        time.sleep(2)
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
        print("тест успешно пройден")
        driver.quit()


