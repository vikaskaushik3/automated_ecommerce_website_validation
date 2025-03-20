import time
import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("setup_driver")
class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.login_page = LoginPage(cls.driver)

    def test_open_portal(self):
        expected_title = r"Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More"
        assert expected_title in self.driver.title

    def test_login_click_submit(self):
        self.login_page.click_login()
        time.sleep(3)

        self.login_page.login_submit()
        verify_element = "//button[normalize-space()='Verify']"
        verify = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, verify_element))
        )
        assert verify.is_displayed()