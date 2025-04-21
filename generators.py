from faker import Faker

fake = Faker()


def generate_courier_creation_body():
    return {
        "login": fake.word(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }


def generate_order_creation_body():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.random_int(min=1, max=50),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=50),
        "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
        "comment": fake.word(),
        "color": fake.random_element(elements=('GREY', 'BLACK'))  # под вопросом
    }
