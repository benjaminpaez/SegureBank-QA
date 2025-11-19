from selenium import webdriver
from registration_page import RegisterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        name = "benjamin1"
        email = "test@user.com"
        password = "testbenjamin"
        confirm_pass = "testbenjamin"
        register = RegisterPage(driver)
        register.open()
        wait
        register.register(name, email, password, confirm_pass)
        wait.until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url
    finally:
        driver.quit()