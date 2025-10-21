from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutInfoPage(BasePage):
    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        super().__init__(driver)

    def is_checkout_page_displayed(self):
        """Checks if the checkout info page is displayed."""
        try:
            title_text = self.get_text(self.PAGE_TITLE)
            return title_text == "Checkout: Your Information"
        except:
            return False

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Fills in all fields on the checkout info page."""
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        """Clicks the 'Continue' button."""
        self.click(self.CONTINUE_BUTTON)