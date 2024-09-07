import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait





from base.base import Base


class MainPage(Base):
    url = 'https://letbefit.ru/'

    phone_field = "//div[@class='input-cont js-switch-cont js-nocoupon-block']//input[@class='input input-mask--phone']"

    order_button = "//div[@class='btn--md btn--mark btn--mobile actionSubmitOrder']"

    def __init__(self, driver):
        self.driver = driver

    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))


    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)


    def landing_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        print('залендились на сайт')


    def input_phone_field(self, phone):
        phone_field_element = self.get_phone_field()
        self.scroll_to_element(phone_field_element)
        phone_field_element.send_keys(phone)
        print('input phone')
        time.sleep(3)



    def click_order_button(self):
        order_button_element = self.get_order_button()
        self.scroll_to_element(order_button_element)
        order_button_element.click()
        print('click order_button')