import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class", autouse=True)
def setup_driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Required for some CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    request.cls.driver = driver
    yield driver
    driver.quit()