from data import DataForCourierCreation, DataForCourierLogin, DataForOrderCreation


def modify_create_courier_body(key, value):
    body = DataForCourierCreation.CREATE_COURIER_BODY.copy()
    body[key] = value
    return body


def modify_courier_login_body(key, value):
    body = DataForCourierLogin.COURIER_LOGIN_BODY.copy()
    body[key] = value
    return body


def modify_create_order_body(key, value):
    body = DataForOrderCreation.CREATE_ORDER_BODY.copy()
    body[key] = value
    return body
