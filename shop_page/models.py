try:
    from Shop.settings import DATABASE
    # модель продукту
    class Product(DATABASE.Model):
        # ідентифікатор продукту
        id = DATABASE.Column(DATABASE.Integer, primary_key = True)
        # назва продукту
        name = DATABASE.Column(DATABASE.String(60))
        # кількість продукту на складі
        count = DATABASE.Column(DATABASE.Integer)
        # ціна продукту
        price = DATABASE.Column(DATABASE.Integer)
        # попередня ціна продукту
        previous_price = DATABASE.Column(DATABASE.Integer)
        # знижка на продукт
        sale = DATABASE.Column(DATABASE.Integer)

        def __repr__(self) -> str:
            return f"id - {self.id}, name - {self.name}"
except Exception as error:
    print(error)
    