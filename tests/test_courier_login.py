import allure
from methods.courier_creation_meth import CourierCreationMeth
from methods.courier_login_meth import CourierLoginMeth
import helpers
from data import ServerResponses, TestData


class TestCourierLogin:
    @allure.title('Тест на успешную авторизацию курьера и получение id')
    def test_successful_courier_login(self, generate_courier):
        with allure.step('Cоздаём курьера'):
            CourierCreationMeth.create_courier(generate_courier)
        with allure.step('Авторизуем курьера'):
            response = CourierLoginMeth.courier_login(generate_courier)
            expected_id = CourierLoginMeth.get_courier_id_by_login_password(generate_courier["login"],
                                                                            generate_courier["password"])
        assert response.status_code == 200 and response.json()["id"] == expected_id

    @allure.title('Тест на невозможность авторизации без обязательного поля Логин')
    def test_without_login_failure(self, generate_courier):
        with allure.step('Создаём курьера'):
            CourierCreationMeth.create_courier(generate_courier)
        with allure.step('Меняем тело авторизации(удаляем логин)'):
            response = CourierLoginMeth.change_auth_body(login=None, password=generate_courier["password"])
        assert response.status_code == 400 and response.json()["message"] == ServerResponses.AUTH_EMPTY_REQUIRED_FIELD

    @allure.title('Тест на ошибку при авторизации с пустым полем Пароль')
    def test_empty_password_failure(self, generate_courier):
        with allure.step('Создаём курьера'):
            CourierCreationMeth.create_courier(generate_courier)
        with allure.step('Меняем тело авторизации(оставляем поле Пароль пустым)'):
            response = CourierLoginMeth.change_auth_body(login=generate_courier["login"], password="")
        assert response.status_code == 400 and response.json()["message"] == ServerResponses.AUTH_EMPTY_REQUIRED_FIELD

    @allure.title('Тест на ошибку при авторизации с неправильным полем Пароль')
    def test_wrong_password_failure(self, generate_courier):
        with allure.step('Создаём курьера'):
            CourierCreationMeth.create_courier(generate_courier)
        with allure.step('Меняем тело авторизации(вставляем в поле Пароль неправильное значение)'):
            response = CourierLoginMeth.change_auth_body(login=generate_courier["login"], password=TestData.AUTH_PASSWORD)
        assert response.status_code == 404 and response.json()["message"] == ServerResponses.AUTH_WRONG_DATA

    @allure.title('Тест на ошибку при авторизации под несуществующим пользователем')
    def test_nonexistent_user_failure(self):
        with allure.step('Создаем данные для авторизации несуществующего пользователя'):
            response = CourierLoginMeth.change_auth_body(login=TestData.AUTH_LOGIN, password=TestData.AUTH_PASSWORD)
        assert response.status_code == 404 and response.json()["message"] == ServerResponses.AUTH_WRONG_DATA
