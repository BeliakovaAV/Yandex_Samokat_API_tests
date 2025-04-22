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


