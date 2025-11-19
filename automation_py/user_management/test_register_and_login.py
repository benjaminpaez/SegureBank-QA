from time import sleep
from selenium import webdriver
from registration_page import RegisterPage
from login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from users import data_users as users

def test_register_and_login():
    num_persona = 9
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        reg= RegisterPage(driver)
        reg.open()
        name = users[num_persona]["name"]
        email = users[num_persona]["email"]
        password = users[num_persona]["password"]
        confirm_pass = users[num_persona]["confirm_pass"]
        reg.register(name, email, password, confirm_pass)
        print("registro existoso")
        sleep(4)
        #Condicional por si el auto-log no funciona
        if "dashboard" not in driver.current_url:
            login = LoginPage(driver)
            login.open()
            print("cond", email,  password)
            login.login(email, password)

        wait.until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url
    finally:
        driver.quit()
