import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, PersonalAccountPageLocators

#Переход по клику на «Личный кабинет». test_successful_navigation_to_personal_account_on_click
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_navigation_to_personal_account_on_click(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
    login_button.click()

    login_button = driver.find_element(By.XPATH, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    login_button.click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, PersonalAccountPageLocators.PERSONAL_ACCOUNT_TEXT)))

    assert "В этом разделе вы можете изменить свои персональные данные" in driver.page_source

#Проверь переход по клику из личного кабинета на «Конструктор» test_successful_navigation_to_constructor_from_personal_account_on_click
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_navigation_to_constructor_from_personal_account_on_click(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
    password_field.send_keys(password)


    login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
    login_button.click()


    login_button = driver.find_element(By.XPATH, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    login_button.click()

    login_button = driver.find_element(By.XPATH, PersonalAccountPageLocators.CONSTRUCTOR_BUTTON)
    login_button.click()

    assert "Оформить заказ" in driver.page_source

#Проверь переход по клику из личного кабинета на логотип Stellar Burgers test_successful_navigation_to_homepage_from_personal_account_on_logo_click№tup", "login_registered_user")
def test_successful_navigation_to_homepage_from_personal_account_on_logo_click(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
    login_button.click()

    login_button = driver.find_element(By.XPATH, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    login_button.click()

    login_button = driver.find_element(By.XPATH, PersonalAccountPageLocators.HEADER_LOGO)
    login_button.click()

    assert "Оформить заказ" in driver.page_source

#Проверь выход по кнопке «Выйти» в личном кабинете. test_successful_logout_from_personal_account
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_logout_from_personal_account(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
    password_field.send_keys(password)


    login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
    login_button.click()


    login_button = driver.find_element(By.XPATH, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    login_button.click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, PersonalAccountPageLocators.LOGOUT_BUTTON)))

    login_button = driver.find_element(By.XPATH, PersonalAccountPageLocators.LOGOUT_BUTTON)
    login_button.click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, LoginPageLocators.LOGIN_TEXT_ENTER)))

    assert "Вход" in driver.page_source
