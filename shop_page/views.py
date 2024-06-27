try:
    import flask
    from .models import *
    from flask_login import current_user

    def render_shop():
        is_name = False
        # перевірка авторизаці користувача
        is_authenticated = False
        is_admin = False
        if current_user.is_authenticated:
            is_admin = current_user.is_admin
            is_authenticated = True
            is_name = current_user.name
        # зчитування куків та кількості товарів у корзині
        cookies = flask.request.cookies.get('product')
        if cookies:
            cookies = cookies.split(' ')
            cookies = len(cookies)
        else:
            cookies = 0
        # відмаляємо сторінку магазину
        return flask.render_template("shop.html", products = Product.query.all(), cookies = cookies, is_admin = is_admin, is_authenticated = is_authenticated, is_name = is_name)
except Exception as error:
    print(error)