import pytest
from selenium import webdriver
import time  # Import the time module


@pytest.fixture(scope="function")
def driver():
    # Setup: Create a new Chrome driver instance
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # 5-second implicit wait

    # Yield the driver to the test function
    yield driver

    # Teardown:
    time.sleep(3)  # <-- THIS IS THE 3-SECOND PAUSE
    driver.quit()