import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Раздел Конструктор успешный переход к разделу Булки test_successful_navigation_to_buns_section_from_constructor
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_navigation_to_buns_section_from_constructor(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
    login_button.click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Соусы']")))

    login_button = driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Соусы']")
    login_button.click()


    login_button = driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Булки']")
    login_button.click()

    assert driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Булки']")

@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_navigation_to_sauces_section_from_constructor(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
    login_button.click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Соусы']")))

    login_button = driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Соусы']")
    login_button.click()

    assert driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Соусы']")

#Раздел Конструктор успешный переход к разделу Начинки test_successful_navigation_to_toppings_section_from_constructor
@pytest.mark.usefixtures("setup", "login_registered_user")
def test_successful_navigation_to_toppings_section_from_constructor(setup, login_registered_user):
    driver = setup
    email, password = login_registered_user

    driver.get("https://stellarburgers.nomoreparties.site/login")

    email_field = driver.find_element(By.XPATH, "//input[@name='name']")
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
    login_button.click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Начинки']")))

    login_button = driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Начинки']")
    login_button.click()


    assert driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Начинки']")
