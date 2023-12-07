from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import USERNAME, PASSWORD 
import os
import pytest


# @pytest.fixture
# Function to create a WebDriver instance and open the Sauce Labs demo website
def initialize_driver():
    driver = webdriver.Edge()
    # Implicit wait for any lag prevention
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    return driver

# Function to perform login and wait for the inventory page
def perform_login(driver, username, password):
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

# Test Case 1: Valid Login
def test_valid_login():
    driver = initialize_driver()
    
    # Replace username and password with another valid set of credentials
    perform_login(driver, USERNAME, PASSWORD)
    
    assert 'https://www.saucedemo.com/inventory.html' == driver.current_url
    
    print("Test Case 1: Valid Login - Passed")
    
    # Close the browser
    driver.quit()

# Test Case 2: Invalid Login
def test_invalid_login():
    driver = initialize_driver()
    
    # Replace username and password with another invalid set of credentials
    perform_login(driver, 'invalid_username', 'invalid_password')
    
    # Check for error message due to invalid username
    error_message = driver.find_element(By.XPATH, '//*[@data-test="error"]').text
    assert "Username and password do not match" in error_message

    print("Test Case 2: Invalid Login - Passed")

    # Close the browser
    driver.quit()

# Test Case 3: Logout
def test_logout():
    driver = initialize_driver()
    
    # Perform a valid login first
    perform_login(driver, USERNAME, PASSWORD)
    
    # Logout
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    
    # Wait for the login page to ensure the logout is successful
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login_button_container"]'))
    )
    
    assert 'https://www.saucedemo.com/' == driver.current_url
    
    print("Test Case 3: Logout - Passed")
    
    # Close the browser
    driver.quit()

# Test Case 4: Add Product to Cart
def test_add_product_to_cart():
    driver = initialize_driver()
    
    # Perform a valid login first
    perform_login(driver, USERNAME, PASSWORD)
    
    # Add a product to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    
    # Verify the product is added to the cart
    cart_indicator = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]')
    assert 'shopping_cart_container' in cart_indicator.get_attribute('class')
    
    print("Test Case 4: Add Product to Cart - Passed")
    
    # Close the browser
    driver.quit()

# Test Case 5: Remove Product from Cart
def test_remove_product_from_cart():
    driver = initialize_driver()
    
    # Perform a valid login first
    perform_login(driver, USERNAME, PASSWORD)
    
    # Add a product to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    
    # Remove the product from the cart
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
    
    # Verify the product is removed from the cart
    cart_indicator = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]')
    assert 'shopping_cart_badge' not in cart_indicator.get_attribute('class')
    
    print("Test Case 5: Remove Product from Cart - Passed")
    
    # Close the browser
    driver.quit()

# Test Case 6: Navigate to About Page
def test_navigate_to_about_page():
    driver = initialize_driver()
    
    # Perform a valid login first
    perform_login(driver, USERNAME, PASSWORD)

    # Open the side menu
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    # Navigate to the About page
    driver.find_element(By.XPATH, '//*[@id="about_sidebar_link"]').click()
    
    
    assert 'https://saucelabs.com/' == driver.current_url
    
    print("Test Case 6: Navigate to About Page - Passed")
    
    # Close the browser
    driver.quit()


if __name__ == "__main__":
    current_file_name = os.path.basename(__file__)
    pytest.main(["-v", "-s", current_file_name, "--html=report.html"])
