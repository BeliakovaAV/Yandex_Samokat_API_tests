import requests
from data import Url


class OrdersListMethod:
    @staticmethod
    def get_orders_list():
        return requests.get(f'{Url.BASE_URL}{Url.ORDER_LIST_URL}')
