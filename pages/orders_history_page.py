import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.locators import OrderLinePageLocators, MainPageLocators


class OrdersHistoryPage(BasePage):
    @allure.step('Ждем загрузки первого заказа из Ленты Заказов')
    def wait_for_orders_loaded(self):
        self.wait_for_element_loaded(OrderLinePageLocators.FIRST_ORDER)

    @allure.step('Проверяем наличие ID заказа в Истории заказов')
    def check_order_id_in_orders_history(self, order_id):
        locator = f"//p[contains(text(), '{order_id}')]"
        try:
            self.driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Кликаем Лента Заказов')
    def click_orders_line(self):
        self.click_element_located(MainPageLocators.ORDER_LINE)