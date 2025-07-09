import allure
from methods.courier_creation_meth import CourierCreationMeth
import helpers
from data import ServerResponses


class TestCreateCourier:
    @allure.title('Тест на успешное создание курьера')
    def test_successful_courier_creation(self, generate_courier):
        with allure.step('Создаём курьера'):
            courier = CourierCreationMeth.create_courier(generate_courier)
        assert courier.status_code == 201 and courier.json() == ServerResponses.COURIER_CREATION_SUCCESS

    @allure.title('Тест на невозможность создания двух одинаковых курьеров')
    def test_double_courier_creation_impossible(self, generate_courier):
        with allure.step('Создаём первого курьера'):
            CourierCreationMeth.create_courier(generate_courier)
        with allure.step('Создаём второго курьера - копию первого'):
            doppelganger = CourierCreationMeth.create_courier(generate_courier)
        assert doppelganger.status_code == 409 and doppelganger.json()["message"] == ServerResponses.SAME_LOGIN_FAILURE

    @allure.title('Тест на ошибку при пустом обязательном поле Логин')
    def test_empty_filed_error(self):
        with allure.step('Создаём курьера без логина'):
            body = helpers.modify_create_courier_body("login", "")
            courier = CourierCreationMeth.create_courier(body)
        assert courier.status_code == 400 and courier.json()["message"] == ServerResponses.COURIER_EMPTY_REQUIRED_FIELD

    @allure.title('Тест на ошибку при пустом обязательном поле Пароль')
    def test_empty_filed_error(self):
        with allure.step('Создаём курьера без пароля'):
            body = helpers.modify_create_courier_body("password", "")
            courier = CourierCreationMeth.create_courier(body)
        assert courier.status_code == 400 and courier.json()["message"] == ServerResponses.COURIER_EMPTY_REQUIRED_FIELD

    @allure.title('Тест на успешное создание курьера без необязательного поля')
    def test_firstname_creation_success(self):
        with allure.step('Создаём курьера без имени(допустимо)'):
            body = helpers.modify_create_courier_body("firstName", "")
            courier = CourierCreationMeth.create_courier(body)
        assert courier.status_code == 201 and courier.json() == ServerResponses.COURIER_CREATION_SUCCESS
