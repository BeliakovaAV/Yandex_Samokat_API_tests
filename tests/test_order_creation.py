import allure
from methods.order_creation_meth import OrderCreationMethod
from generators import generate_order_creation_body
import helpers
import pytest


class TestCreateOrder:
    @allure.title('Тест на создание заказа с одним цветом, двумя цветами, без цвета')
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order_with_various_colors(self, colors):
        with allure.step('Создаём тело запроса'):
            order_body = generate_order_creation_body()
            if colors is not None:
                order_body["color"] = colors
        with allure.step('Создаём заказ'):
            response = OrderCreationMethod.create_order(order_body)
        with allure.step('Проверяем наличие track'):
            expected_track = OrderCreationMethod.get_order_track_number(response)
        assert response.status_code == 201 and response.json()["track"] == expected_track

    @allure.title('Тест на создание заказа с одним цветом, двумя цветами, без цвета')
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order_with_various_colors(self, colors, cleanup_order):
        with allure.step('Создаём тело запроса'):
            order_body = generate_order_creation_body()
            if colors is not None:
                order_body["color"] = colors
        with allure.step('Создаём заказ'):
            response = OrderCreationMethod.create_order(order_body)
        with allure.step('Проверяем наличие track'):
            expected_track = response.json()['track']
            cleanup_order(expected_track)
        assert response.status_code == 201 and response.json()["track"] == expected_track
