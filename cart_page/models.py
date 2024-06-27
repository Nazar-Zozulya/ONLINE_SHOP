try:
    from Shop.settings import DATABASE
    # модель замовлення
    class Cart(DATABASE.Model):
        # ідентифікатор замовлення
        id = DATABASE.Column(DATABASE.Integer, primary_key = True)
        # ім'я клієнта
        name = DATABASE.Column(DATABASE.Text)
        # прізвище клієнта
        surname = DATABASE.Column(DATABASE.Text)
        # номер телефону клієнта
        number = DATABASE.Column(DATABASE.Integer)
        # електронна пошта клієнта
        email = DATABASE.Column(DATABASE.Text)
        # місто замовлення
        city = DATABASE.Column(DATABASE.Text)
        # відділення Нової пошти замовлення
        post_office = DATABASE.Column(DATABASE.Integer)
        # додаткові побажання замовлення
        additional_wish = DATABASE.Column(DATABASE.Text)
        # статус замовлення (виконане/не виконане)
        status = DATABASE.Column(DATABASE.Boolean, nullable = False)

        def __repr__(self) -> str:
            return f"name: {self.name}"
except Exception as error:
    print(error)