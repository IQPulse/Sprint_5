import pytest
from selenium.webdriver.common.by import By


# Вход по кнопке «Войти в аккаунт» на главной test_successful_login_via_homepage
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_login_via_homepage(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/")

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    login_button.click()

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
    login_button.click()

    assert "Войти в аккаунт" not in driver.page_source

#Вход через кнопку «Личный кабинет» test_successful_login_via_personal_account_button
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_login_via_personal_account_button(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/")

    login_button = driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    login_button.click()

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
    login_button.click()

    assert "Войти в аккаунт" not in driver.page_source

#Вход через кнопку в форме регистрации test_successful_login_via_registration_form
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_login_via_registration_form(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/register")

    login_button = driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]")
    login_button.click()

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
    login_button.click()

    assert "Войти в аккаунт" not in driver.page_source

#Вход через кнопку в форме регистрации test_successful_login_via_registration_form
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_login_via_password_recovery_form(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    login_button = driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]")
    login_button.click()

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
    login_button.click()

    assert "Войти в аккаунт" not in driver.page_source