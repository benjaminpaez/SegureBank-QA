from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.url = "https://v0-banking-system-debugging.vercel.app/login"
    
    email = (By.ID, "email")
    password = (By.ID, "password")
    submit = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        self.driver.get(self.url)
    
    def login(self, email_value, password_value):
        self.wait.until(EC.presence_of_element_located(self.email)).send_keys(email_value)
        self.wait.until(EC.presence_of_element_located(self.password)).send_keys(password_value)
        self.wait.until(EC.element_to_be_clickable(self.submit)).click()