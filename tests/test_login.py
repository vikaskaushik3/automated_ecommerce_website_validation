import time
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_open_portal(web_driver):
    driver = web_driver
    LoginPage(driver)
    driver.implicitly_wait(5)

    expected_title = r"Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More"
    assert expected_title in driver.title


def test_login_click_submit(web_driver):
    login_page = LoginPage(web_driver)
    login_page.click_login()
    time.sleep(3)

    login_page.login_submit()
    verify_element = "//button[normalize-space()='Verify']"
    verify = WebDriverWait(web_driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, verify_element))
    )
    assert verify.is_displayed()