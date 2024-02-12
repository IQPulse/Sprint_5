import pytest
from selenium import webdriver
from helpers import generate_user_data
from data import login_registered_user_data, login_bad_password_data


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_registered_user():
    return login_registered_user_data

@pytest.fixture(scope="module")
def login_bad_password():
    return login_bad_password_data

@pytest.fixture(scope="module")
def login_not_registered_user():
    name, email, password = generate_user_data()
    return name, email, password
