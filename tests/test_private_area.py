from pages.profile_page import ProfilePage
from pages.entrance_page import EntrancePage
from pages.main_page import MainPage
import allure
from data.urls import URLS


class TestPrivateArea:
    @allure.title('По клику на личный кабинет переходим на Личный Кабинет')
    def test_main_page_route_to_private_area(self, driver, make_user, create_user_payload):
        entrance_page = EntrancePage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.wait_for_entrance_page_header_loaded()
        entrance_page.enter_email(payload["email"])
        entrance_page.enter_password(payload["password"])
        entrance_page.click_enter_button()
        entrance_page.check_page()
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.click_private_area_button()
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_header_loaded()

        assert profile_page.check_page(URLS.PROFILE_PAGE_SUBDIRECTORY)

    @allure.title('Из личного кабинета можно перейти в Историю Заказов')
    def test_private_area_route_to_history(self, driver, make_user, create_user_payload):
        entrance_page = EntrancePage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.click_private_area_button()
        main_page.check_page(URLS.PROFILE_PAGE_SUBDIRECTORY)
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_header_loaded()
        profile_page.check_page(URLS.PROFILE_PAGE_SUBDIRECTORY)
        profile_page.click_orders_history_section_name()

        assert entrance_page.check_page(URLS.ORDER_HISTORY_SUBDIRECTORY)

    @allure.title('Из личного кабинета можно Выйти из аккаунта')
    def test_account_logout(self, driver, make_user, create_user_payload):
        entrance_page = EntrancePage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.click_private_area_button()
        main_page.check_page(URLS.PROFILE_PAGE_SUBDIRECTORY)
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_header_loaded()
        profile_page.check_page(URLS.PROFILE_PAGE_SUBDIRECTORY)
        profile_page.click_exit()
        entrance_page.check_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        entrance_page.wait_for_entrance_page_header_loaded()
        entrance_page.click_constructor()
        entrance_page.check_page()
        main_page.wait_for_main_page_header_loaded()

        assert main_page.check_enter_account_button()
