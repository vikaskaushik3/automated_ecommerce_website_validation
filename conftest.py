import pytest
from selenium import webdriver


@pytest.fixture(scope="module", autouse=True)
def web_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()



