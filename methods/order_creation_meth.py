import requests
from data import Url


class OrderCreationMethod:
    @staticmethod
    def create_order(body):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER_CREATION_URL}', json=body)

    @staticmethod
    def cancel_order(order_track):
        payload = {"track": order_track}
        return requests.put(f'{Url.BASE_URL}{Url.ORDER_CANCEL_URL}', json=payload)

    @staticmethod
    def get_order_track_number(response):
        return response.json().get("track")
