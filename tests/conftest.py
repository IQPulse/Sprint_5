import pytest
from selenium import webdriver
import random

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_registered_user():
    return "anton_nazarov_5_002@ya.ru", "123456"

@pytest.fixture(scope="module")
def login_bad_password():
    return "anton_nazarov_5_003", "anton_nazarov_5_003@ya.ru", "12345"


@pytest.fixture(scope="module")
def login_not_registered_user():
    name, email, password = generate_user_data()
    return name, email, password


def generate_user_data():
    base_name = "anton_nazarov_5_"
    random_number = str(random.randint(10, 999999)).zfill(6)
    name = f"{base_name}{random_number}"
    email = f"{name}@ya.ru"
    password = "123456"
    return name, email, password