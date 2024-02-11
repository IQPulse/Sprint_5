import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators

#Раздел Конструктор успешный переход к разделу Булки test_successful_navigation_to_buns_section_from_constructor
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_navigation_to_buns_section_from_constructor(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
    login_button.click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, MainPageLocators.SAUCES_BUTTON)))

    login_button = driver.find_element(By.XPATH, MainPageLocators.SAUCES_BUTTON)
    login_button.click()


    login_button = driver.find_element(By.XPATH, MainPageLocators.BUNS_BUTTON)
    login_button.click()

    assert driver.find_element(By.XPATH, MainPageLocators.CURRENT_BUNS_SECTION)

@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_navigation_to_sauces_section_from_constructor(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
    login_button.click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, MainPageLocators.SAUCES_BUTTON)))

    login_button = driver.find_element(By.XPATH, MainPageLocators.SAUCES_BUTTON)
    login_button.click()

    assert driver.find_element(By.XPATH, MainPageLocators.CURRENT_SAUCES_SECTION)

#Раздел Конструктор успешный переход к разделу Начинки test_successful_navigation_to_toppings_section_from_constructor
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_navigation_to_toppings_section_from_constructor(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
    login_button.click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, MainPageLocators.TOPPINGS_BUTTON)))

    login_button = driver.find_element(By.XPATH, MainPageLocators.TOPPINGS_BUTTON)
    login_button.click()


    assert driver.find_element(By.XPATH, MainPageLocators.CURRENT_TOPPINGS_SECTION)
