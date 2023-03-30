import time
import allure
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

@allure.description("Test link about")
def test_link_about(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\Diana\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, chrome_options=options)

    print("Start test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()


    # time.sleep(10)











