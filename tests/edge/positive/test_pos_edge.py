
from browser_factory.browser_factory import BrowserFactory
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage
from pages.order_confirm_page import OrderConfirmPage


def test_pos_edge():
    browser = "edge"
    driver = BrowserFactory(browser).get_driver()

    print("Начинаем позитивный тест по оформлению заказа на Edge")

    try:
        main_page = MainPage(driver)
        main_page.landing_page()
        main_page.input_phone_field("9085543490")
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
        driver.quit()
        print("тест успешно пройден")

test_pos_edge()