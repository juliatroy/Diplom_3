from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import allure
from data.locators import OrderLinePageLocators, MainPageLocators


class OrderLinePage(BasePage):

    @allure.step('Ждем загрузки заголовка страницы Ленты Заказов')
    def wait_for_orders_line_header_loaded(self):
        self.wait_for_element_loaded(OrderLinePageLocators.ORDER_LINE_HEADER)

    @allure.step('Получаем ID первого заказа')
    def get_first_order_id(self):
        return self.driver.find_element(By.XPATH, OrderLinePageLocators.FIRST_ORDER[1]).text

    @allure.step('Кликаем заказ Ленты Заказов по номеру {order_id}')
    def click_order_by_id(self, order_id):
        locator = f"//p[text()='{order_id}']"
        selector = (By.XPATH, locator)
        self.click_element_located(selector)

    @allure.step('Проверяем видимость модального окна')
    def check_order_details_modal_opened(self):
        try:
            self.driver.find_element(By.XPATH, OrderLinePageLocators.ORDER_DETAILS_MODAL)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Получаем ID заказа из заголовка модального окна')
    def get_order_id_from_modal(self):
        return self.driver.find_element(By.XPATH, OrderLinePageLocators.ORDER_DETAILS_MODAL_ORDER_ID_XPATH).text

    @allure.step('Проверяем наличие ID {order_id} заказа в Ленте заказов')
    def check_order_id_in_orders_line(self, order_id):
        locator = f"//p[contains(text(), '{order_id}')]"
        try:
            self.driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Нажимаем Конструктор')
    def click_constructor(self):
        return self.click_element_located(MainPageLocators.MENU_CONSTRUCTOR)

    @allure.step('Получаем значение счетчика Выполнено за все время')
    def get_total_count(self):
        return self.driver.find_element(By.XPATH, OrderLinePageLocators.TOTAL_COUNT_XPATH).text

    @allure.step('Получаем значение счетчика Выполнено за сегодня')
    def get_today_count(self):
        return self.driver.find_element(By.XPATH, OrderLinePageLocators.TODAY_COUNT_XPATH).text

    @allure.step('Проверяем наличие ID {order_id} заказа среди заказов в работе')
    def check_order_id_in_processing_orders(self, order_id):
        locator = f"//li[text()='{order_id}']"
        try:
            self.driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            return False
        return True


