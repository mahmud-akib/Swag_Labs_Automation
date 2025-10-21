from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutOverviewPage(BasePage):
    # Locators
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        super().__init__(driver)

    def click_finish(self):
        """Clicks the 'Finish' button."""
        self.click(self.FINISH_BUTTON)