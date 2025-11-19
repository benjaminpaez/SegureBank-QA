from time import sleep
from decimal import Decimal
from selenium import webdriver

from user_management.register_and_login import register_login
from .models import Account, Transfer
from .dashboard import Dashboard

def test_transfer_update_balance():
    driver = webdriver.Chrome()
    try:
        num_persona = 9
        data_user = register_login(driver, num_persona)
        email = data_user["email"]

        dash = Dashboard(driver)
        dash.wait_loaded()
        initial_bal = dash.get_balance()

        account_origin = Account(
            email=email,
            balance=initial_bal
        )

        amount_transfer = Decimal("100.00")
        accoun_dest = "1236554485556655212"

        transf = Transfer(
            origin= account_origin,
            destination=accoun_dest,
            amount=amount_transfer
        )

        transf.apply()
        expected_bal = account_origin.balance

        transfer_page = dash.go_to_transfer()
        transfer_page.wait_loaded()
        transfer_page.make_transfer(accoun_dest, amount_transfer)

        sleep(2)
        dash.open()
        dash.wait_loaded()
        final_balance = dash.get_balance()

        assert final_balance == expected_bal, (
            f"Saldo final incorrecto.\n"
            f"Saldo esperado: {expected_bal}\n"
            f"Saldo final: {final_balance}"
        )
        print("Transfencia y actualizacion de saldos corracto")
    finally:
        driver.quit()