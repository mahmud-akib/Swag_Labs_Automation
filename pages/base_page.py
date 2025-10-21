from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


# This is a base class for all Page Objects
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # 10-second explicit wait

    def go_to_page(self, url):
        """Navigates to a specific URL."""
        self.driver.get(url)

    def find_element(self, locator):
        """Finds a single element, waiting until it's visible."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        """Finds all elements matching a locator, waiting until they are visible."""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        """Clicks a web element, waiting until it's clickable."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        """Sends text to an input field."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Gets the text from an element."""
        element = self.find_element(locator)
        return element.text

    def hover_to_element(self, locator):
        """Hovers the mouse over a specific element."""
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def select_dropdown_by_visible_text(self, locator, text):
        """Selects an option from a dropdown by its visible text."""
        select_element = Select(self.find_element(locator))
        select_element.select_by_visible_text(text)