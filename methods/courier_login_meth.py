import requests
from data import Url
from .courier_creation_meth import CourierCreationMeth


class CourierLoginMeth:

    @staticmethod
    def courier_login(body):
        payload = {
            "login": body["login"],
            "password": body["password"]
        }
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN_URL}', json=payload)

    @staticmethod
    def get_courier_id_by_login_password(login, password):
        params = {'login': login, 'password': password}
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN_URL}', json=params)
        logins = response.json()
        return logins["id"]

    @staticmethod
    def change_auth_body(login=None, password=None):
        payload = {}
        if login is not None:
            payload["login"] = login
        if password is not None:
            payload["password"] = password
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN_URL}', json=payload)


