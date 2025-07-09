from methods.orders_list_meth import OrdersListMethod
import allure


class TestOrderList:
    @allure.title('Тест на получение списка заказов')
    def test_order_list_return(self):
        response = OrdersListMethod.get_orders_list()
        assert response.status_code == 200 and "orders" in response.json()