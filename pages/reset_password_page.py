from pages.password_recovery_page import PasswordRecoveryPage
from data.locators import ResetPasswordPageLocators

import allure


class PasswordResetPage(PasswordRecoveryPage):
    @allure.step('Нажимаем на кнопку Показать пароль')
    def show_password_click(self):
        self.click_element_located(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверяем активность поля ввода пароля')
    def show_password_check(self):
        return self.find_element_located(ResetPasswordPageLocators.ACTIVE_PASSWORD_INPUT_FIELD)

