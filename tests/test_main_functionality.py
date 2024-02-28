from pages.entrance_page import EntrancePage
from pages.main_page import MainPage
from pages.order_line_page import OrderLinePage
import allure
from data.urls import URLS


class TestMainFunctionality:
    @allure.title('Из личного кабинета можно перейти в Конструктор')
    def test_redirect_to_constructor(self, driver):
        entrance_page = EntrancePage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        entrance_page.click_constructor()
        entrance_page.check_page()
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()

        assert main_page.check_page()

    @allure.title('Из основной страницы можно перейти в Ленту Заказов')
    def test_redirect_to_orders_line(self, driver):
        entrance_page = EntrancePage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        entrance_page.click_constructor()
        entrance_page.check_page()
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.click_orders_line()
        order_line = OrderLinePage(driver)

        assert order_line.check_page(URLS.ORDER_LINE_SUBDIRECTORY)

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_to_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_main_page_header_loaded()
        main_page.click_first_ingredient()

        assert main_page.check_modal_opened()

    @allure.title('Всплывающее окно с деталями закрывается крестиком')
    def test_click_to_x_closes_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_main_page_header_loaded()
        main_page.click_first_ingredient()
        main_page.wait_modal_header_loaded()
        main_page.click_close_modal()

        assert not main_page.check_modal_opened()

    @allure.title('Добавление ингредиента в заказы увеличивает счетчик этого ингредиента')
    def test_drag_and_drop_ingredient_to_basket_increases_ingredient_count(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_for_main_page_header_loaded()
        initial_value = main_page.get_first_ingredient_counter_value()
        main_page.drag_n_drop_first_ingredient_to_basket()
        updated_value = main_page.get_first_ingredient_counter_value()

        assert initial_value < updated_value

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_make_order(self, driver, make_user, create_user_payload):
        entrance_page = EntrancePage(driver)
        entrance_page.open_page(URLS.ENTRANCE_PAGE_SUBDIRECTORY)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        entrance_page.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_for_main_page_header_loaded()
        main_page.check_make_order_button()
        main_page.drag_n_drop_first_ingredient_to_basket()
        main_page.click_make_order()

        assert main_page.check_modal_opened()



