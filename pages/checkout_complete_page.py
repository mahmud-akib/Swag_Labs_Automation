from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutCompletePage(BasePage):
    # Locators
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver)

    def get_complete_header_text(self):
        """Gets the text of the 'Thank You' header."""
        return self.get_text(self.COMPLETE_HEADER)

    def click_back_home(self):
        """Clicks the 'Back Home' button."""
        self.click(self.BACK_HOME_BUTTON)