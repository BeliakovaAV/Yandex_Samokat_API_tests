import requests
from data import Url


class CourierCreationMeth:
    @staticmethod
    def create_courier(body):
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_CREATION_URL}', json=body)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.COURIER_CREATION_URL}/{courier_id}')
