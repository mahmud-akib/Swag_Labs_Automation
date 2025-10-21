from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    # Locators
    APP_LOGO = (By.CLASS_NAME, "app_logo")
    SHOPPING_CART_LINK = (By.ID, "shopping_cart_container")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    ADD_BACKPACK_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_FROM_CART_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    def is_logo_displayed(self):
        """Checks if the app logo is displayed on the page."""
        try:
            self.find_element(self.APP_LOGO)
            return True
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def click_burger_menu(self):
        """Clicks the top-left burger menu button."""
        self.click(self.BURGER_MENU_BUTTON)

    def click_logout_link(self):
        """Clicks the 'Logout' link from the sidebar menu."""
        self.click(self.LOGOUT_LINK)

    def logout(self):
        """Performs a full logout flow."""
        self.click_burger_menu()
        self.click_logout_link()

    def add_backpack_to_cart(self):
        """Adds the 'Sauce Labs Backpack' to the cart."""
        self.click(self.ADD_BACKPACK_TO_CART_BUTTON)

    def remove_backpack_from_cart(self):
        """Removes the 'Sauce Labs Backpack' from the cart."""
        self.click(self.REMOVE_BACKPACK_FROM_CART_BUTTON)

    def get_cart_badge_count(self):
        """Gets the text from the cart's badge. Returns None if badge isn't found."""
        try:
            return self.get_text(self.SHOPPING_CART_BADGE)
        except:
            return None

    def click_cart_icon(self):
        """Clicks the shopping cart icon to go to the cart page."""
        self.click(self.SHOPPING_CART_LINK)

    def sort_items_by(self, visible_text):
        """Selects a sorting option from the dropdown."""
        self.select_dropdown_by_visible_text(self.SORT_DROPDOWN, visible_text)

    def get_item_prices(self):
        """Gets a list of all item prices, converted to floats."""
        price_elements = self.find_elements(self.ITEM_PRICE)
        prices = []
        for element in price_elements:
            # Remove '$' sign and convert to float
            prices.append(float(element.text.replace("$", "")))
        return prices