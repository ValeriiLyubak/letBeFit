from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base


class OrderConfirmPage(Base):

    order_complited_message = "//div[@class='type--w700 type--xl type--center mb-12']"

    def get_confirm_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_complited_message)))

    def get_order_confirm_message(self):
        confirm_message_element = self.get_confirm_message()
        message = confirm_message_element.text
        print(message)
        return message