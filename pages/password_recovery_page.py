from pages.base_page import BasePage
import allure
from data.locators import PasswordRecoveryPageLocators


class PasswordRecoveryPage(BasePage):

    @allure.step('Ждем загрузки заголовка страницы Восстановления пароля')
    def wait_for_recovery_page_header_loaded(self):
        self.wait_for_element_loaded(PasswordRecoveryPageLocators.HEADER_RESTORE_PASSWORD)

    @allure.step('Вводим имейл')
    def enter_email(self, email):
        self.send_keys_to_element_located(locator=PasswordRecoveryPageLocators.EMAIL_INPUT_FIELD, keys=email)

    @allure.step('Нажимаем кнопку восстановления пароля')
    def recover_button_click(self):
        self.click_element_located(PasswordRecoveryPageLocators.BUTTON_RESTORE_PASSWORD)
