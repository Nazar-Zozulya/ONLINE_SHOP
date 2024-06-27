try:
    import flask_login
    from .settings import shop_app
    from registration_page.models import User
    # встановлення секретного ключа для захисту сесі
    shop_app.secret_key = '192837465'
    # встановлення менеджера авторизації з Flask-Login
    login_manager = flask_login.LoginManager(app = shop_app)
    # вказуємо, на яку сторінку буде перенаправлено користувача, якщо не авторизований
    login_manager.login_view = "login"

    # функція для завантаження користувача
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)
except Exception as error:
    print(error)