import pytest

from generators import generate_courier_creation_body
from methods.courier_login_meth import CourierLoginMeth
from methods.courier_creation_meth import CourierCreationMeth


@pytest.fixture
def generate_courier():
    courier_body = generate_courier_creation_body()
    yield courier_body
    courier_id = CourierLoginMeth.get_courier_id_by_login_password(courier_body["login"], courier_body["password"])
    CourierCreationMeth.delete_courier(courier_id)


@pytest.fixture
def generate_booking():
    booking_body = generate_booking_body()
    booking_response = BookingMethods.create_booking(booking_body)
    booking_id = booking_response.json()['bookingid']
    yield booking_id
