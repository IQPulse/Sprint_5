import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, RegistrationPageLocators
from data import login_not_registered_user, login_bad_password
from config import BASE_URL

class TestRegistration:
    @pytest.mark.usefixtures("driver", "login_not_registered_user")
    def test_successful_registration(self, driver, login_not_registered_user):
        name, email, password = login_not_registered_user

        driver.get(f"{BASE_URL}/register")

        name_field = driver.find_element(By.XPATH, RegistrationPageLocators.LOGIN_INPUT)
        name_field.send_keys(name)

        email_field = driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_INPUT)
        email_field.send_keys(email)

        password_field = driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)

        register_button = driver.find_element(By.XPATH, RegistrationPageLocators.REGISTER_BUTTON)
        register_button.click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, LoginPageLocators.LOGIN_TEXT_ENTER)))

        assert "Вход" in driver.page_source

    @pytest.mark.usefixtures("driver", "login_bad_password")
    def test_error_for_incorrect_password(self, driver, login_bad_password):
        name, email, password = login_bad_password

        driver.get("https://stellarburgers.nomoreparties.site/register")

        name_field = driver.find_element(By.XPATH, RegistrationPageLocators.LOGIN_INPUT)
        name_field.send_keys(name)

        email_field = driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_INPUT)
        email_field.send_keys(email)

        password_field = driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_INPUT)
        password_field.send_keys(password)

        register_button = driver.find_element(By.XPATH, RegistrationPageLocators.REGISTER_BUTTON)
        register_button.click()

        assert "Некорректный пароль" in driver.page_source
