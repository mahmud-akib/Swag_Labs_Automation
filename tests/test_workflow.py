import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


# Make sure all tests are INDENTED inside this class
class TestWorkflow:

    # --- Test 1 ---
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.go_to_login_page()
        login_page.login("standard_user", "secret_sauce")

        assert inventory_page.is_logo_displayed()
        assert "inventory.html" in inventory_page.get_current_url()

    # --- Test 2 ---
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)

        login_page.go_to_login_page()
        login_page.login("locked_out_user", "secret_sauce")

        expected_error = "Epic sadface: Sorry, this user has been locked out."
        assert expected_error in login_page.get_error_message()

    # --- Test 3 (This was likely indented WRONG) ---
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.go_to_login_page()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.logout()

        assert login_page.is_login_page_displayed()

    # --- Test 4 (This was likely indented WRONG) ---
    def test_add_item_to_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.go_to_login_page()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack_to_cart()

        assert inventory_page.get_cart_badge_count() == "1"

    # --- Test 5 (This was likely indented WRONG) ---
    def test_remove_item_from_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.go_to_login_page()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack_to_cart()

        inventory_page.remove_backpack_from_cart()

        assert inventory_page.get_cart_badge_count() is None

    # --- Test 6 (This was likely indented WRONG) ---
    def test_view_cart_with_item(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.go_to_login_page()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack_to_cart()

        inventory_page.click_cart_icon()

        assert cart_page.is_item_in_cart("Sauce Labs Backpack")

    # --- Test 7 (This was indented CORRECTLY) ---
    def test_start_checkout_process(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_info_page = CheckoutInfoPage(driver)

        login_page.go_to_login_page()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack_to_cart()

        inventory_page.click_cart_icon()
        cart_page.click_checkout()

        assert checkout_info_page.is_checkout_page_displayed()

    # --- Test 8 ---
    def test_sort_price_low_to_high(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.go_to_login_page()
        login_page.login("standard_user", "secret_sauce")

        # Sort by "Price (low to high)"
        inventory_page.sort_items_by("Price (low to high)")

        # Get list of prices and check if it's sorted
        prices = inventory_page.get_item_prices()
        assert prices == sorted(prices)

    # --- Test 9 (This was indented CORRECTLY) ---
    def test_checkout_end_to_end_success(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_info_page = CheckoutInfoPage(driver)
        checkout_overview_page = CheckoutOverviewPage(driver)
        checkout_complete_page = CheckoutCompletePage(driver)

        # 1. Login and add item
        login_page.go_to_login_page()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack_to_cart()

        # 2. Go to cart and start checkout
        inventory_page.click_cart_icon()
        cart_page.click_checkout()

        # 3. Fill info and continue
        checkout_info_page.fill_checkout_info("Test", "User", "1s2345")
        checkout_info_page.click_continue()

        # 4. Finish checkout
        checkout_overview_page.click_finish()

        # 5. Assert
        assert "Thank you for your order" in checkout_complete_page.get_complete_header_text()

    # --- Test 10 (This was indented CORRECTLY) ---
    def test_checkout_back_home(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_info_page = CheckoutInfoPage(driver)
        checkout_overview_page = CheckoutOverviewPage(driver)
        checkout_complete_page = CheckoutCompletePage(driver)

        # 1. Complete the full checkout flow
        login_page.go_to_login_page()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack_to_cart()
        inventory_page.click_cart_icon()
        cart_page.click_checkout()
        checkout_info_page.fill_checkout_info("Test", "User", "12345")
        checkout_info_page.click_continue()
        checkout_overview_page.click_finish()

        # 2. Click "Back Home"
        checkout_complete_page.click_back_home()

        # 3. Assert
        assert inventory_page.is_logo_displayed()
        assert "inventory.html" in inventory_page.get_current_url()
