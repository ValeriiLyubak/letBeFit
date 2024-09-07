import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base







class CheckoutPage(Base):

    name_field = "//input[@class='input' and @data-placeholder='Имя']"

    email_field = "//input[@class='input' and @data-placeholder='Email (обязательно)']"

    address_field = "//input[@class='input active-address']"

    cash_button = "//div[@class='tab__el js-tick' and @data-test='orderCash']"

    confirm_button = "//div[@class='btn--md btn--mark btn--mobile action-send-order']"

    empty_name_field = "//div[@class='input-msg' and text()='Поле обязательно к заполнению']"

    empty_email_field = "//div[@class='input-msg' and text()='Введите корректный email']"

    def get_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_address_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_field)))

    def get_cash_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cash_button)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    def get_empty_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.empty_name_field)))

    def get_empty_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.empty_email_field)))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)


    def input_name_field(self, name):
        name_field_element = self.get_name_field()
        self.scroll_to_element(name_field_element)
        name_field_element.send_keys(name)
        print('input name')
        time.sleep(3)

    def input_email_field(self, email):
        self.get_email_field().send_keys(email)
        print('input email')
        time.sleep(3)


    def input_address_field(self, address):
        address_field_element = self.get_address_field()
        self.scroll_to_element(address_field_element)
        address_field_element.send_keys(address)
        print('input address')
        time.sleep(3)


    def click_cash_button(self):
        cash_button_element = self.get_cash_button()
        self.scroll_to_element(cash_button_element)
        cash_button_element.click()
        print('click cash_button')


    def click_confirm_button(self):
        confirm_button_element = self.get_confirm_button()
        self.scroll_to_element(confirm_button_element)
        confirm_button_element.click()
        print('click confirm_button')


    def get_empty_name_field_message(self):
        empty_name_field_message_element = self.get_empty_name_field()
        self.scroll_to_element(empty_name_field_message_element)
        empty_name_message = empty_name_field_message_element.text
        print(empty_name_message)
        return empty_name_message

    def get_empty_email_field_message(self):
        empty_email_field_message_element = self.get_empty_email_field()
        self.scroll_to_element(empty_email_field_message_element)
        empty_email_message = empty_email_field_message_element.text
        print(empty_email_message)
        return empty_email_message