class MainPageLocators:
    # Локатор кнопки "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = "//button[contains(text(),'Войти в аккаунт')]"

    # Локатор кнопки "Личный Кабинет" на главной странице
    PERSONAL_ACCOUNT_BUTTON = "//p[contains(text(),'Личный Кабинет')]"

    # Локатор кнопки "Соусы" в меню
    SAUCES_BUTTON = "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Соусы']"

    # Локатор кнопки "Булки" в меню
    BUNS_BUTTON = "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Булки']"

    # Локатор текущего выбранного раздела "Булки"
    CURRENT_BUNS_SECTION = "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Булки']"

    # Локатор текущего выбранного раздела "Соусы"
    CURRENT_SAUCES_SECTION = "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Соусы']"

    # Локатор кнопки "Начинки" в меню
    TOPPINGS_BUTTON = "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Начинки']"

    # Локатор текущего выбранного раздела "Начинки"
    CURRENT_TOPPINGS_SECTION = "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text()='Начинки']"


class LoginPageLocators:
    # Локатор поля ввода email на странице входа
    EMAIL_INPUT = "//input[@name='name']"

    # Локатор поля ввода пароля на странице входа
    PASSWORD_INPUT = "//label[contains(text(),'Пароль')]/following-sibling::input"

    # Локатор кнопки "Войти" на странице входа
    LOGIN_BUTTON = "//button[contains(text(),'Войти')]"

    # Локатор текста "Вход" на странице входа
    LOGIN_TEXT_ENTER = "//h2[contains(text(),'Вход')]"


class RegistrationPageLocators:
    # Локатор ссылки "Войти" на странице Регистрации
    LOGIN_LINK = "//a[contains(text(),'Войти')]"

    # Локатор поля ввода логина
    LOGIN_INPUT = "(//input[@name='name'])[1]"

    # Локатор поля ввода email
    EMAIL_INPUT = "(//input[@name='name'])[2]"

    # Локатор поля ввода пароля
    PASSWORD_INPUT = "//input[@name='Пароль']"

    # Локатор кнопки "Зарегистрироваться"
    REGISTER_BUTTON = "//button[contains(text(),'Зарегистрироваться')]"

class PasswordRecoveryPageLocators:
    # Локатор ссылки "Войти" на странице Восстановления пароля
    LOGIN_LINK = "//a[contains(text(),'Войти')]"


class PersonalAccountPageLocators:
    # Локатор текста "В этом разделе вы можете изменить свои персональные данные"
    PERSONAL_ACCOUNT_TEXT = "//p[@class='Account_text__fZAIn text text_type_main-default']"

    # Локатор кнопки "Конструктор"
    CONSTRUCTOR_BUTTON = "//p[contains(text(),'Конструктор')]"

    # Локатор Логотипа в шапке сайта
    HEADER_LOGO = "//div[@class='AppHeader_header__logo__2D0X2']//a//*[name()='svg']"

    # Локатор кнопки "Выход"
    LOGOUT_BUTTON = "//button[contains(text(),'Выход')]"

    # Локатор текста "Вход" на странице входа
    LOGIN_TEXT_ENTER = "//h2[contains(text(),'Вход')]"