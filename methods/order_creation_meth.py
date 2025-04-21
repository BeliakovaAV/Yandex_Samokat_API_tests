import requests
from data import Url, DataForOrderCreation


class OrderCreationMethod:
    @staticmethod
    def create_order():
        return requests.post(f'{Url.BASE_URL}{Url.ORDER_CREATION_URL}', json=DataForOrderCreation.CREATE_ORDER_BODY)


