import pytest
from helpers import generate_user_data

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