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