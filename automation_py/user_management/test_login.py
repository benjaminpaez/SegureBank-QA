from selenium import webdriver
from login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        email = "email1@test.com"
        password = "12345678"
        login = LoginPage(driver)
        login.open()
        wait
        login.login(email, password)
        wait.until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url
    finally:
        driver.quit()