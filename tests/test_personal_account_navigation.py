from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    MainPageLocators,
    LoginPageLocators,
    PersonalAccountPageLocators
)
from data import login_registered_user
from config import BASE_URL

class TestPersonalAccountNavigation:
    def test_successful_navigation_to_personal_account_on_click(self, driver, login_registered_user):
        email, password = login_registered_user

        driver.get(f"{BASE_URL}/login")

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

    def test_successful_navigation_to_constructor_from_personal_account_on_click(self, driver, login_registered_user):
        email, password = login_registered_user

        driver.get(f"{BASE_URL}/login")

        email_field = driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT)
        email_field.send_keys(email)

        password_field = driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)


        login_button = driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON)
        login_button.click()


        login_button = driver.find_element(By.XPATH, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        login_button.click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, PersonalAccountPageLocators.CONSTRUCTOR_BUTTON)))

        login_button = driver.find_element(By.XPATH, PersonalAccountPageLocators.CONSTRUCTOR_BUTTON)
        login_button.click()

        assert "Оформить заказ" in driver.page_source

    def test_successful_navigation_to_homepage_from_personal_account_on_logo_click(self, driver, login_registered_user):
        email, password = login_registered_user

        driver.get(f"{BASE_URL}/login")

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

    def test_successful_logout_from_personal_account(self, driver, login_registered_user):
        email, password = login_registered_user

        driver.get(f"{BASE_URL}/login")

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
