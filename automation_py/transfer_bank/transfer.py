from decimal import Decimal
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Transfer:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    FORM = (By.CSS_SELECTOR, "form[class='space-y-5']")
    DESTINATION = (By.ID, "recipient")
    AMOUNT = (By.ID, "amount")
    BTN_CONFIRM = (By.CSS_SELECTOR, "button[type='submit']")

    def wait_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.FORM))
    
    def make_transfer(self, destination: str, amount: Decimal):
        input_dest = self.wait.until(EC.presence_of_element_located(self.DESTINATION))
        input_amount = self.wait.until(EC.presence_of_element_located(self.AMOUNT))
        btn_confirm = self.wait.until(EC.element_to_be_clickable(self.BTN_CONFIRM))
        
        input_dest.clear()
        input_dest.send_keys(destination)

        input_amount.clear()
        input_amount.send_keys(str(amount))

        btn_confirm.click()
