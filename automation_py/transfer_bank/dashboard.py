from decimal import Decimal
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://v0-banking-system-debugging.vercel.app/"

class Dashboard:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.url = f"{URL}/dashboard"
    
    BALANCE = (By.CSS_SELECTOR, "h2[class='text-4xl font-bold text-[#1a1a1a]']")
    BTN_TRANSFER = (By.LINK_TEXT, 'Transfer Money')

    def open(self):
        self.driver.get(self.url)
    
    def wait_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.BALANCE))
    
    def get_balance(self) -> Decimal:
        element = self.wait.until(EC.visibility_of_element_located(self.BALANCE))
        text = element.text
        return self._parser_balance(text)
    
    def go_to_transfer(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.BTN_TRANSFER))
        btn.click()
        from .transfer import Transfer
        return Transfer(self.driver)

    @staticmethod    
    def _parser_balance(text: str) -> Decimal:
        clean = text.replace("$", "").replace(" ", "").strip()
        return Decimal(clean)
    