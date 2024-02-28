from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок на главной странице
    PRIVATE_AREA = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Главная страница, кнопка перехода в Личный кабинет
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка на главной странице, доступная
    # только после входа пользователя в аккаунт
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка Войти в аккаунт на гл. странице
    MENU_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка Конструктор на хедере главной страницы
    ORDER_LINE = (By.XPATH, "//p[text() = 'Лента Заказов']")  # Кнопка Лента Заказов на хедере главной страницы

    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]")
    FIRST_INGREDIENT_COUNTER_XPATH = "//p[contains(@class, 'counter_counter')][1]"
    INGREDIENT_MODAL_XPATH = "//section[contains(@class, 'Modal_modal_opened_')]"
    CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_MODAL_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")  # Общий локатор для корзины
    TEMPORARY_ORDER_MODAL_HEADER = (By.XPATH, "//h2[text()='9999']")
    ORDER_ID_XPATH = "//h2[contains(@class, 'Modal_modal__title')]"


class EntrancePageLocators:
    ENTRANCE_HEADER = (By.XPATH, ".//h2[text()='Вход']")  # Заголовок формы логина
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # Гиперссылка для восстановления пароля
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # Поле ввода e-mail
    PASSWORD_INPUT_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::*")  # Поле ввода пароля
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа на форме логина


class ProfilePageLocators:
    BUTTON_EXIT_ACCOUNT = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из аккаунта
    ORDERS_HISTORY_AREA = (By.XPATH, "//a[text()='История заказов']")  # Кнопка секции истории заказов
    PROFILE_AREA = (By.XPATH, "//a[text()='Профиль']")  # Кнопка секции истории заказов


class PasswordRecoveryPageLocators:
    HEADER_RESTORE_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']")  # Хедер страницы восстан. пароля
    BUTTON_ENTER_ACCOUNT_FROM_RESTORE_FORM = (By.XPATH, "//a[text()='Войти']")  # Кнопка входа в аккаунт на форме
    # восстановления пароля
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")  # Поле ввода e-mail
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка выхода из аккаунта


class ResetPasswordPageLocators:
    HEADER_RESTORE_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']")  # Хедер страницы восстан. пароля
    # с кодом из письма
    SHOW_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon')]")
    ACTIVE_PASSWORD_INPUT_FIELD = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")


class OrderLinePageLocators:
    ORDER_LINE_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")  # Хедер страницы ленты заказов
    FIRST_ORDER = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]/a/div/p[contains(@class, "
                                "'text_type_digits')]")
    ORDER_DETAILS_MODAL = ".//div[contains(@class, 'Modal_orderBox')]"
    ORDER_DETAILS_MODAL_ORDER_ID_XPATH = ".//div[contains(@class, 'Modal_orderBox')]/p"
    TOTAL_COUNT_XPATH = "//p[text()='Выполнено за все время:']/following-sibling::p"
    TODAY_COUNT_XPATH = "//p[text()='Выполнено за сегодня:']/following-sibling::p"

class OrdersHistoryPageLocators:
    FIRST_ORDERS_HISTORY_ORDER = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]/a/div/p[contains(@class, "
                                "'text_type_digits')]")




