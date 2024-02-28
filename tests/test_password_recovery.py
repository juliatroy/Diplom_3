from pages.entrance_page import EntrancePage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.reset_password_page import PasswordResetPage
import allure
from data.urls import URLS


class TestPasswordRecovery:
    @allure.title('По кнопке Восстановить пароль переходим на страницу восстановления пароля')
    def test_password_recovery_brings_to_recovery_page(self, driver):
        entrance_page = EntrancePage(driver)
        entrance_page.open_page(subdir=URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        entrance_page.wait_for_entrance_page_header_loaded()
        entrance_page.click_restore_password()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.wait_for_recovery_page_header_loaded()

        assert password_recovery_page.check_page(subdir=URLS.RECOVER_PASSWORD_SUBDIRECTORY)

    @allure.title('По кнопке Восстановить пароль переходим на страницу восстановления пароля')
    def test_password_reset_for_valid_email(self, driver, make_user, create_user_payload):
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_page(subdir=URLS.RECOVER_PASSWORD_SUBDIRECTORY)
        password_recovery_page.wait_for_recovery_page_header_loaded()
        email = payload["email"]
        password_recovery_page.enter_email(email)
        password_recovery_page.recover_button_click()
        reset_password_page = PasswordResetPage(driver)
        reset_password_page.wait_for_recovery_page_header_loaded()

        assert reset_password_page.check_page(subdir=URLS.RECOVER_PASSWORD_SUBDIRECTORY)

    @allure.title('Кнопка "Показать пароль" делает поле ввода пароля активным')
    def test_password_reset_gets_highlighted(self, driver, make_user, create_user_payload):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_page(URLS.RECOVER_PASSWORD_SUBDIRECTORY)
        password_recovery_page.wait_for_recovery_page_header_loaded()
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        email = payload["email"]
        password_recovery_page.enter_email(email)
        password_recovery_page.recover_button_click()
        reset_password_page = PasswordResetPage(driver)
        reset_password_page.wait_for_recovery_page_header_loaded()
        reset_password_page.check_page(subdir=URLS.RESET_PASSWORD_SUBDIRECTORY)
        reset_password_page.show_password_click()

        assert reset_password_page.show_password_check()







