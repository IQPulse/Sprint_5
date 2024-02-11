import random
# Генерация рандомных данных для регистрации
def generate_user_data():
    base_name = "anton_nazarov_5_"
    random_number = str(random.randint(10, 999999)).zfill(6)
    name = f"{base_name}{random_number}"
    email = f"{name}@ya.ru"
    password = "123456"
    return name, email, password