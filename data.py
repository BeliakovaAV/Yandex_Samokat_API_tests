class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_CREATION_URL = '/api/v1/courier'
    COURIER_LOGIN_URL = '/api/v1/courier/login'
    ORDER_CREATION_URL = '/api/v1/orders'
    ORDER_CANCEL_URL = '/api/v1/orders/cancel'
    ORDER_LIST_URL = '/api/v1/orders'


class DataForCourierCreation:
    CREATE_COURIER_BODY = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }


class ServerResponses:
    COURIER_CREATION_SUCCESS = {"ok": True}
    SAME_LOGIN_FAILURE = "Этот логин уже используется"
    COURIER_EMPTY_REQUIRED_FIELD = "Недостаточно данных для создания учетной записи"
    AUTH_EMPTY_REQUIRED_FIELD = "Недостаточно данных для входа"
    AUTH_WRONG_DATA = "Учетная запись не найдена"


class TestData:
    AUTH_PASSWORD = "647364732"
    AUTH_LOGIN = "krasopetka"
