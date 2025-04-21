import allure
from methods.courier_creation_meth import CourierCreationMeth
from methods.courier_login_meth import CourierLoginMeth
import helpers

class TestCourierLogin:
    @allure.title('Тест на успешную авторизацию курьера')
    def test_successful_courier_login(self, generate_courier):
        with allure.step('Cоздаём курьера'):
            CourierCreationMeth.create_courier(generate_courier)
            response = CourierLoginMeth.courier_login(generate_courier)
            expected_id = CourierLoginMeth.get_courier_id_by_login_password(generate_courier["login"], generate_courier["password"])
        assert response.status_code == 200 and response.json()["id"] == expected_id
