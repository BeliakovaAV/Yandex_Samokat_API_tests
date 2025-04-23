import pytest

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


def generate_order():
    order_body = generate_order_creation_body()
    new_order = OrderCreationMethod.create_order(order_body)
    yield new_order
    order_track = OrderCreationMethod.get_order_track_number(new_order)
    OrderCreationMethod.cancel_order(order_track)

