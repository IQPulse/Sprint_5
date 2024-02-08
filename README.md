# Sprint_5
Финальный проект 5 спринт

# Автотесты для сервиса Stellar Burgers

## Описание проекта

Данный проект представляет собой набор автоматизированных тестов для веб-сервиса "Stellar Burgers". 
[Stellar Burgers](https://stellarburgers.nomoreparties.site/) - это космический фастфуд, где пользователи могут собрать и заказать бургер из необычных ингредиентов.


## Запуск тестов

Для запуска всех тестов выполните следующую команду:

pytest tests/


## Описание тестов

### Тесты по Регистрации (test_registration.py)

1. **Успешная регистрация** (`test_successful_registration`)
2. **Ошибка для некорректного пароля** (`test_error_for_incorrect_password`)

### Тесты по Входу в аккаунт (test_login.py)

1. **Вход по кнопке «Войти в аккаунт» на главной** (`test_successful_login_via_homepage`)
2. **Вход через кнопку «Личный кабинет»** (`test_successful_login_via_personal_account_button`)
3. **Вход через кнопку в форме регистрации** (`test_successful_login_via_registration_form`)
4. **Вход через кнопку в форме восстановления пароля** (`test_successful_login_via_password_recovery_form`)

### Личный кабинет (test_personal_account_navigation.py)

1. **Переход по клику на «Личный кабинет»** (`test_successful_navigation_to_personal_account_on_click`)
2. **Проверь переход по клику из личного кабинета на «Конструктор»** (`test_successful_navigation_to_constructor_from_personal_account_on_click`)
3. **Проверь переход по клику из личного кабинета на логотип Stellar Burgers** (`test_successful_navigation_to_homepage_from_personal_account_on_logo_click`)
4. **Проверь выход по кнопке «Выйти» в личном кабинете** (`test_successful_logout_from_personal_account`)

### Собери бургер (test_constructor.py)

1. **Раздел Конструктор успешный переход к разделу Булки** (`test_successful_navigation_to_buns_section_from_constructor`)
2. **Раздел Конструктор успешный переход к разделу Соусы** (`test_successful_navigation_to_sauces_section_from_constructor`)
3. **Раздел Конструктор успешный переход к разделу Начинки** (`test_successful_navigation_to_toppings_section_from_constructor`)

