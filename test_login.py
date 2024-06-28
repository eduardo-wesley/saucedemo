import time
import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class Teste01:
        def test_login_(self):
                driver = conftest.driver
                driver.find_element(By.ID, "user-name").send_keys('standard_user')
                driver.find_element(By.ID, "password").send_keys('secret_sauce')
                driver.find_element(By.ID,"login-button").click()
                time.sleep(2)

                # Add compras ao carrinho

                driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[3]/button').click()
                driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[2]/div[3]/button').click()
                time.sleep(2)

                # Click carrinho

                driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]').click()
                time.sleep(2)

                # CheckOut

                driver.find_element(By.XPATH,'//*[@id="cart_contents_container"]/div/div[2]/a[2]').click()
                time.sleep(2)

                # CheckOut infromation

                driver.find_element(By.XPATH,'//*[@id="first-name"]').send_keys('José')
                driver.find_element(By.XPATH,'//*[@id="last-name"]').send_keys('Pedro')
                driver.find_element(By.XPATH,'//*[@id="postal-code"]').send_keys('123456789')
                driver.find_element(By.XPATH,'//*[@id="checkout_info_container"]/div/form/div[2]/input').click()
                time.sleep(2)
