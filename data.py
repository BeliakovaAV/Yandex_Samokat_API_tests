class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_CREATION_URL = '/api/v1/courier'
    COURIER_LOGIN_URL = '/api/v1/courier/login'
    ORDER_CREATION_URL = '/api/v1/orders'
    ORDER_LIST_URL = '/api/v1/orders'


class DataForCourierCreation:
    CREATE_COURIER_BODY = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }


class DataForCourierLogin:
    COURIER_LOGIN_BODY = {
        "login": "ninja",
        "password": "1234"
    }


class DataForOrderCreation:
    CREATE_ORDER_BODY = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
