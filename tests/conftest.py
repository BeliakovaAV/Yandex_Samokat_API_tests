import pytest
import allure

from generators import generate_courier_creation_body, generate_order_creation_body
from methods.courier_login_meth import CourierLoginMeth
from methods.courier_creation_meth import CourierCreationMeth
from methods.order_creation_meth import OrderCreationMethod


@pytest.fixture
def generate_courier():
    courier_body = generate_courier_creation_body()
    yield courier_body
    courier_id = CourierLoginMeth.get_courier_id_by_login_password(courier_body["login"], courier_body["password"])
    CourierCreationMeth.delete_courier(courier_id)


@pytest.fixture
def cleanup_order():
    order_tracks = []

    def register_order_track(order_track):
        order_tracks.append(order_track)

    yield register_order_track

    for order_track in order_tracks:
        with allure.step('Удаляем созданное бронирование'):
            OrderCreationMethod.cancel_order(order_track)
