import time

from browser_factory.browser_factory import BrowserFactory
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage
from pages.order_confirm_page import OrderConfirmPage


def test_pos_mobile():
    browser = "chrome"
    emulate_device = "iPhone X"
    driver = BrowserFactory(browser, emulate_device=emulate_device).get_driver()

    print("Начинаем позитивный тест по оформлению заказа на эмуляции iPhone X в Chrome")

    try:
        main_page = MainPage(driver)
        main_page.landing_page()
        time.sleep(2)
        main_page.input_phone_field("9085543490")
        time.sleep(2)
        main_page.click_order_button()
        checkout_page = CheckoutPage(driver)
        checkout_page.input_name_field("Тест")
        checkout_page.input_email_field("testmail@gmail.com")
        checkout_page.input_address_field("Москва")
        checkout_page.click_cash_button()
        checkout_page.click_confirm_button()
        order_confirm_page = OrderConfirmPage(driver)
        actual_message = order_confirm_page.get_order_confirm_message()
        expected_message = "Спасибо за заказ"
        assert expected_message == actual_message, f"Ожидалось '{expected_message}', но получили '{actual_message}'"
    finally:
        print("Тест успешно пройден")
        driver.quit()
