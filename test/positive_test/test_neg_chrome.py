from browser_factory.browser_factory import BrowserFactory
from pages.main_page import MainPage


def test_neg_chrome():
    browser = "chrome"
    driver = BrowserFactory(browser).get_driver()

    print("Начинаем позитивный тест по оформлению заказа на Chrome")

    try:
        main_page = MainPage(driver)
        main_page.landing_page()
        main_page.click_order_button()
        actual_message = main_page.get_empty_phone_field_allert_message()
        expected_message = "Введите корректный телефон"
        assert expected_message == actual_message, f"Ожидалось '{expected_message}', но получили '{actual_message}'"
    finally:
        driver.quit()
        print("тест успешно пройден")


test_neg_chrome()