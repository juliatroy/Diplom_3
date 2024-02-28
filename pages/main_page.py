from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Ждем загрузки заголовка главной страницы проекта')
    def wait_for_main_page_header_loaded(self):
        self.wait_for_element_loaded(MainPageLocators.MAIN_PAGE_HEADER)

    @allure.step('Кликаем по кнопке Личный кабинет')
    def click_private_area_button(self):
        self.click_element_located(MainPageLocators.PRIVATE_AREA)

    @allure.step('Проверяем наличие кнопки Войти в аккаунт, видимой только для незалогиненного пользователя')
    def check_enter_account_button(self):
        return self.find_element_located(MainPageLocators.BUTTON_ENTER_ACCOUNT)

    @allure.step('Проверяем наличие кнопки Оформить заказ, видимой только для незалогиненного пользователя')
    def check_make_order_button(self):
        return self.find_element_located(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Кликаем Лента Заказов')
    def click_orders_line(self):
        self.click_element_located(MainPageLocators.ORDER_LINE)

    @allure.step('Кликаем первый ингредиент на главной странице')
    def click_first_ingredient(self):
        self.click_element_located(MainPageLocators.FIRST_INGREDIENT)

    @allure.step('Проверяем видимость модального окна')
    def check_modal_opened(self):
        try:
            self.driver.find_element(By.XPATH, MainPageLocators.INGREDIENT_MODAL_XPATH)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Ждем загрузки заголовка модального окна')
    def wait_modal_header_loaded(self):
        self.wait_for_element_loaded(MainPageLocators.INGREDIENT_MODAL_HEADER)

    @allure.step('Нажимаем на крестик, закрывающий модальное окно')
    def click_close_modal(self):
        self.click_element_located(MainPageLocators.CLOSE_MODAL)

    @allure.step('Получаем значение счетчика ингредиента')
    def get_first_ingredient_counter_value(self):
        return self.driver.find_element(By.XPATH, MainPageLocators.FIRST_INGREDIENT_COUNTER_XPATH).text

    @allure.step('Перетаскиваем первый ингредиент в корзину')
    def drag_n_drop_first_ingredient_to_basket(self):
        self.do_drag_n_drop(source=MainPageLocators.FIRST_INGREDIENT, target=MainPageLocators.BASKET)

    @allure.step('Кликаем Оформить заказ')
    def click_make_order(self):
        self.click_element_located(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Получаем значение ID заказа при его оформлении')
    def get_order_id_when_created(self):
        self.wait_until_element_not_present(MainPageLocators.TEMPORARY_ORDER_MODAL_HEADER)
        return self.driver.find_element(By.XPATH, MainPageLocators.ORDER_ID_XPATH).text

    @allure.step('Получаем значение ID заказа при его оформлении')
    def make_order_and_check_modal_open(self):
        self.check_make_order_button()
        self.drag_n_drop_first_ingredient_to_basket()
        self.click_make_order()
        self.check_modal_opened()








