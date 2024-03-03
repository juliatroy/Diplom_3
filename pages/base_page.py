from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import URLS
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу по URL')
    def open_page(self, subdir=''):
        url = URLS.MAIN_PAGE_URL+subdir
        return self.driver.get(url)

    @allure.step('Проверяем текущий url')
    def check_page(self, subdir=''):
        combined_url = URLS.MAIN_PAGE_URL + subdir
        return self.driver.current_url == combined_url

    @allure.step('Ждем загрузки заголовка страницы')
    def wait_for_element_loaded(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    @allure.step('Ищем элемент по локатору')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    @allure.step('Вводим текст в элемент')
    def send_keys_to_element_located(self, locator, time=10, keys=None):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                               message=f'Element not found in {locator}')
        self.find_element_located(locator).send_keys(keys)

    @allure.step('Кликаем по элементу')
    def click_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}').click()

    @allure.step('Получаем текст, находящийся по локатору')
    def get_text_by_locator(self, locator):
        return self.find_element_located(locator).text

    @allure.step('Драг-н-дроп элемента на элемент')
    def do_drag_n_drop(self, source, target):
        drag = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(source))
        drop = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(target))
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step('Ждем исчезновения элемента из DOMа')
    def wait_until_element_not_present(self, locator, time=10):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))



