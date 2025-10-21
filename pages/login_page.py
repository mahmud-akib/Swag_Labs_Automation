from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    URL = "https://www.saucedemo.com/v1/"

    def __init__(self, driver):
        super().__init__(driver)

    # Page actions
    def go_to_login_page(self):
        """Navigates to the login page."""
        self.go_to_page(self.URL)

    def enter_username(self, username):
        """Enters the username."""
        self.send_keys(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enters the password."""
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Clicks the login button."""
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Gets the login error message text."""
        return self.get_text(self.ERROR_MESSAGE)

    def login(self, username, password):
        """Performs a full login action."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_login_page_displayed(self):
        """Checks if the login button is displayed to confirm we are on the login page."""
        try:
            self.find_element(self.LOGIN_BUTTON)
            return True
        except:
            return False