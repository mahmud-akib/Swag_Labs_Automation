# SauceDemo Test Automation Project

This is a UI test automation project for the website `https://www.saucedemo.com/v1/`.

It is built using **Python**, **Selenium**, and **pytest**, following the **Page Object Model (POM)** design pattern. The project covers end-to-end (E2E) user workflows, including login, sorting, adding items to the cart, and the full checkout process.

## Technologies Used

* **Python 3.x**
* **Selenium**: For browser automation and interaction.
* **pytest**: As the test runner for test discovery, execution, and assertions.
* **pytest-html**: For generating a detailed HTML test report.

## Features & Test Cases

This suite includes 10 automated test cases covering the following user flows:

1.  **test_valid_login**:                 Verifies successful login with valid credentials.
2.  **test_invalid_login**:               Verifies the correct error message is shown for a locked-out user.
3.  **test_logout**:                      Verifies a user can successfully log in and then log out.
4.  **test_add_item_to_cart**:            Verifies that a user can add a specific item to the shopping cart.
5.  **test_remove_item_from_cart**:       Verifies that a user can add an item and then remove it from the inventory page.
6.  **test_view_cart_with_item**:         Verifies that an added item appears correctly in the cart page.
7.  **test_start_checkout_process**:      Verifies navigation from the cart to the "Checkout: Your Information" page.
8.  **test_sort_price_low_to_high**:      Verifies that the product sorting filter for "Price (low to high)" works correctly.
9.  **test_checkout_end_to_end_success**: Verifies the complete, end-to-end checkout process.
10. **test_checkout_back_home**:          Verifies that the "Back Home" button on the "Checkout Complete" page returns the user to the inventory.

## Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

* Python 3.8 or newer.
* Google Chrome browser.

### 2. Clone the Repository

Clone this project to your local machine:
```bash
git clone [https://github.com/mahmud-akib/saucedemo_test.git](https://github.com/mahmud-akib/saucedemo_test.git)
cd saucedemo_test
````

### 3\. Create a Virtual Environment (Recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4\. Install Dependencies

Install all the required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 5\. Download ChromeDriver

This project requires the Selenium ChromeDriver to interact with the Chrome browser.

1.  Find your Google Chrome version (Go to `chrome://settings/help`).
2.  Download the matching **ChromeDriver** executable from the [Chrome for Testing dashboard](https://googlechromelabs.github.io/chrome-for-testing/).
3.  Unzip the file and place the `chromedriver.exe` (or `chromedriver`) in the root of your `saucedemo_test` project folder.

## How to Run Tests

All tests are run from the root directory (`saucedemo_test/`) using `pytest`.

### Run All Tests in Terminal

This will run all 10 tests and print the results (dots for passes, `F` for failures) to your terminal.

```bash
pytest
```

### Run Tests and Generate HTML Report

This will run all 10 tests and create a file named `test_report.html` with a detailed, shareable summary of the results.

```bash
pytest --html=test_report.html
```

## View the Report

After running the command above, a file named **`test_report.html`** will appear in your project folder. Double-click this file to open it in any web browser and see the detailed test results.

-----

## Project Structure

```
saucedemo_test/
├── pages/
│   ├── base_page.py               # Base class with common Selenium methods
│   ├── login_page.py              # Page Object for Login
│   ├── inventory_page.py          # Page Object for Products/Inventory
│   ├── cart_page.py               # Page Object for Shopping Cart
│   ├── checkout_info_page.py      # Page Object for Checkout Step 1
│   ├── checkout_overview_page.py  # Page Object for Checkout Step 2
│   └── checkout_complete_page.py  # Page Object for Checkout Finish
├── tests/
│   ├── conftest.py                # pytest fixture (driver setup/teardown & 3s pause)
│   └── test_workflow.py           # All 10 test cases
├── requirements.txt               # Project dependencies
└── README.md                      # You are here!
```

```
```
