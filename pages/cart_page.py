from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    # Locators
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def is_item_in_cart(self, item_name):
        """Checks if a specific item is in the cart by its name."""
        try:
            cart_items = self.find_elements(self.ITEM_NAME)
            for item in cart_items:
                if item.text == item_name:
                    return True
            return False
        except:
            return False

    def click_checkout(self):
        """Clicks the 'Checkout' button."""
        self.click(self.CHECKOUT_BUTTON)