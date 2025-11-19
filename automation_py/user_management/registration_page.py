from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class RegisterPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.url = "https://v0-banking-system-debugging.vercel.app/signup"
    
    name = (By.ID, "name") 
    email = (By.ID, "email")
    password = (By.ID, "password")
    confirmPassword = (By.ID, "confirmPassword")
    createAccount = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        self.driver.get(self.url)

    def register(self, name_value, email_value, password_value, confirmPassword_value):
        self.wait.until(EC.presence_of_element_located(self.name)).send_keys(name_value)
        self.wait.until(EC.presence_of_element_located(self.email)).send_keys(email_value)
        self.wait.until(EC.presence_of_element_located(self.password)).send_keys(password_value)
        self.wait.until(EC.presence_of_element_located(self.confirmPassword)).send_keys(confirmPassword_value)
        self.wait.until(EC.presence_of_element_located(self.createAccount)).click()

    
