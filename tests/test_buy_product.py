import time
import allure
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

# @pytest.mark.run(order=3)
@allure.description("Test buy product 1")
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\Diana\\PycharmProjects\\resource\\chromedriver.exe')
    # driver = webdriver.Chrome(service=s, chrome_options=options)
    driver = webdriver.Chrome(service=s, options=options)

    print("Start test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.click_finish_button()

    f = Finish_page(driver)
    f.finish()

    print("Finish test")
    driver.quit()


    # enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
    # enter_shopping_cart.click()
    # print("Click enter shopping cart")

# @pytest.mark.run(order=1)
@allure.description("Test buy product 2")
def test_buy_product_2(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\Diana\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, chrome_options=options)

    print("Start test 2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

# @pytest.mark.run(order=2)
@allure.description("Test buy product 3")
def test_buy_product_3(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\Diana\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, chrome_options=options)

    print("Start test 3")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()


    # time.sleep(10)










