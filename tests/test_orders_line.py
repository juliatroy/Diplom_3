from pages.order_line_page import OrderLinePage
from pages.main_page import MainPage
from pages.entrance_page import EntrancePage
from pages.profile_page import ProfilePage
from pages.orders_history_page import OrdersHistoryPage
import allure
from data.urls import URLS


class TestOrdersLine:
    @allure.title('Eсли кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_opens_order_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_main_page_header_loaded()
        main_page.click_orders_line()
        orders_line = OrderLinePage(driver)
        orders_line.wait_for_orders_line_header_loaded()
        order_id = orders_line.get_first_order_id()
        orders_line.click_order_by_id(order_id)
        new_id = orders_line.get_order_id_from_modal()
        assert orders_line.check_order_details_modal_opened() and order_id == new_id

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_new_order_appears_in_orders_line(self, driver, make_user, create_user_payload):
        entrance_page = EntrancePage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.make_order()
        order_id = main_page.get_order_id_when_created()
        main_page.click_close_modal()
        main_page.click_private_area_button()
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_header_loaded()
        profile_page.click_orders_history_section_name()
        orders_history = OrdersHistoryPage(driver)
        orders_history.wait_for_orders_loaded()
        assert orders_history.check_order_id_in_orders_history(order_id)
        orders_history.click_orders_line()
        orders_line = OrderLinePage(driver)
        orders_line.wait_for_orders_line_header_loaded()

        assert orders_line.check_order_id_in_orders_line(order_id)

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_new_order_increases_total_and_todays_orders_count(self, driver, make_user, create_user_payload):
        entrance_page = EntrancePage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.click_orders_line()
        orders_line = OrderLinePage(driver)
        orders_line.wait_for_orders_line_header_loaded()
        total_count = orders_line.get_total_count()
        today_count = orders_line.get_today_count()
        orders_line = OrderLinePage(driver)
        orders_line.click_constructor()
        main_page.make_order()
        main_page.click_close_modal()
        main_page.click_orders_line()
        orders_line.wait_for_orders_line_header_loaded()
        new_total_count = orders_line.get_total_count()
        new_today_count = orders_line.get_today_count()
        assert new_total_count > total_count and new_today_count > today_count

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_new_order_appears_in_processing_orders(self, driver, make_user, create_user_payload):
        entrance_page = EntrancePage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.make_order()
        order_id = main_page.get_order_id_when_created()
        main_page.click_close_modal()
        main_page.click_orders_line()
        orders_line = OrderLinePage(driver)
        orders_line.wait_for_orders_line_header_loaded()
        assert orders_line.check_order_id_in_processing_orders(order_id)




