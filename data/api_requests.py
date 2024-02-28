import requests
import allure

class BaseRequests:
    host = 'https://stellarburgers.nomoreparties.site'

    def exec_post_request_and_check(self, url, data, status):
        response = requests.post(url=url, data=data)
        assert response.status_code == status
        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text

    def exec_delete_request_and_check(self, url, status, token):
        headers = {"Content-Type": "application/json", 'authorization': token}
        response = requests.delete(url=url, headers=headers)
        assert response.status_code == status
        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text


class UserRequests(BaseRequests):
    user_handler = '/api/auth/register'
    manipulate_user_handler = '/api/auth/user'

    @allure.step('Создаем пользователя, отправив запрос POST. Ожидаем статус респонса {status}')
    def post_create_user(self, data=None, status=200):
        url = f"{self.host}{self.user_handler}"
        return self.exec_post_request_and_check(url, data=data, status=status)

    @allure.step('Удаляем пользователя, отправив запрос DELETE. Ожидаем статус респонса {status}')
    def delete_user(self, token=None, status=202):
        url = f"{self.host}{self.manipulate_user_handler}"
        return self.exec_delete_request_and_check(url, status=status, token=token)
