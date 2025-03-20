import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage():
    _base_url = "https://flipkart.com"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self._base_url)

    def click_login(self):
        login_xpath = "//span[normalize-space()='Login']"
        login_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, login_xpath))
        )

        # Move the cursor to an empty space before clicking
        action = ActionChains(self.driver)
        action.move_by_offset(10, 10).click().perform()
        time.sleep(2)  # Allow time for the tooltip to disappear
        login_button.click()

    def login_submit(self):
        otp_element = self.driver.find_element(By.XPATH, "//input[@class='r4vIwl BV+Dqf']")
        otp_element.send_keys("7838351517")
        self.driver.implicitly_wait(5)

        submit_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Request OTP']")
        submit_button.click()
        time.sleep(3)