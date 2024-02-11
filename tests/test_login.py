import pytest
from selenium.webdriver.common.by import By
from locators import (
    MainPageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    PasswordRecoveryPageLocators
)
from data import login_registered_user

@pytest.mark.usefixtures("setup", "login_registered_user")
class TestLoginPage:
    def test_successful_login_via_homepage(self, setup, login_registered_user):
        driver = setup
        email, password = login_registered_user

        driver.get("https://stellarburgers.nomoreparties.site/")

        login_button = driver.find_element(By.XPATH, MainPageLocators.LOGIN_BUTTON)
        login_button.click()

        email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
        email_field.send_keys(email)

        password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)

        login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        assert "Войти в аккаунт" not in driver.page_source

    def test_successful_login_via_personal_account_button(self, setup, login_registered_user):
        driver = setup
        email, password = login_registered_user

        driver.get("https://stellarburgers.nomoreparties.site/")

        login_button = driver.find_element(By.XPATH, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        login_button.click()

        email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
        email_field.send_keys(email)

        password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)

        login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        assert "Войти в аккаунт" not in driver.page_source

    def test_successful_login_via_registration_form(self, setup, login_registered_user):
        driver = setup
        email, password = login_registered_user

        driver.get("https://stellarburgers.nomoreparties.site/register")

        login_button = driver.find_element(By.XPATH, RegistrationPageLocators.LOGIN_LINK)
        login_button.click()

        email_field = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
        email_field.send_keys(email)

        password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)

        login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        assert "Войти в аккаунт" not in driver.page_source

    def test_successful_login_via_password_recovery_form(self, setup, login_registered_user):
        driver = setup
        email, password = login_registered_user

        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        login_button = driver.find_element(By.XPATH, PasswordRecoveryPageLocators.LOGIN_LINK)
        login_button.click()

        email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
        email_field.send_keys(email)

        password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)

        login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        assert "Войти в аккаунт" not in driver.page_source
