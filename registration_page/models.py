try:
    from Shop.settings import DATABASE
    from flask_login import UserMixin
    # модель користувача
    class User(DATABASE.Model, UserMixin):
        # ідентифікатор користувача
        id = DATABASE.Column(DATABASE.Integer, primary_key = True)
        # ім'я користувача
        name = DATABASE.Column(DATABASE.String(50),nullable = False)
        # електронна пошта користувача
        email = DATABASE.Column(DATABASE.String(256),nullable = False)
        # пароль користувача
        password = DATABASE.Column(DATABASE.String(256), nullable = False)  
        # чи є адмін? 0 - ні, 1 - так
        is_admin = DATABASE.Column(DATABASE.Boolean, nullable = False)
        def __repr__(self) -> str:
            return f"User - {self.name}, id - {self.id}"
        
        def is_authenticated(self):
            return True
        
        def is_active(self): 
            return True

        def get_id(self):
            return self.id
except Exception as error:
    print(error)