import pytest
import allure
from selenium import webdriver
from faker import Faker
from selenium.webdriver.chrome.service import Service
from data.api_requests import UserRequests
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

fake = Faker()

# @allure.step('Открываем браузер')
# @pytest.fixture(params=['chrome', 'firefox'])
# def driver(request):
#     if request.param == 'chrome':
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service)
#     elif request.param == 'firefox':
#         service = Service(GeckoDriverManager().install())
#         driver = webdriver.Firefox(service=service)
#
#     yield driver
#     driver.quit()

@allure.step('Открываем браузер')
@pytest.fixture()
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
#     elif request.param == 'firefox':
#         service = Service(GeckoDriverManager().install())
#         driver = webdriver.Firefox(service=service)
#
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def make_user():
    user = {}

    def _make_user(data):
        nonlocal user
        user_requests = UserRequests()
        user = user_requests.post_create_user(data=data)
        return user

    yield _make_user
    UserRequests().delete_user(token=user['accessToken'])


@pytest.fixture
def create_user_payload():
    @allure.step('Конструируем payload для пользователя')
    def _create_user_payload(name=None, email=None, password=None):
        payload = {}
        if name == 'rand':
            payload["name"] = fake.name()
        elif name is not None:
            payload["name"] = name
        if password == 'rand':
            payload["password"] = fake.name()
        elif password is not None:
            payload["password"] = password
        if email == 'rand':
            payload["email"] = fake.email()
        elif email is not None:
            payload["email"] = email
        return payload

    return _create_user_payload
