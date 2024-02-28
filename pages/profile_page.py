import allure
from pages.base_page import BasePage
from data.locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step('Нажимаем заголовок секции Истории заказов')
    def click_orders_history_section_name(self):
        return self.click_element_located(ProfilePageLocators.ORDERS_HISTORY_AREA)

    @allure.step('Ждем загрузки заголовка секции Профиль')
    def wait_for_profile_header_loaded(self):
        return self.wait_for_element_loaded(ProfilePageLocators.PROFILE_AREA)

    @allure.step('Нажимаем Выход')
    def click_exit(self):
        return self.click_element_located(ProfilePageLocators.BUTTON_EXIT_ACCOUNT)


