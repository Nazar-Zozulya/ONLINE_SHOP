try:
    import flask
    from Shop.settings import DATABASE
    from shop_page.models import Product
    from flask_login import current_user

    def render_home():
        cookies = flask.request.cookies.get('product')
        if cookies:
            cookies = cookies.split(' ')
            cookies = len(cookies)
        else:
            cookies = 0
        if flask.request.method == "POST":
            # додавання нового товару до бази даних
            product = Product(
                            name = flask.request.form['name'],
                            price = flask.request.form['price'],
                            sale = flask.request.form['sale'],
                            description = flask.request.form['description'],
                            count = flask.request.form['count']
                            )
            DATABASE.session.add(product)
            DATABASE.session.commit()
        is_name = False
        is_authenticated = False
        is_admin = False
        # перевірка авторизації користувача
        if current_user.is_authenticated:
            is_admin = current_user.is_admin
            is_authenticated = True
            is_name = current_user.name
        # відображення головної сторінки 
        return flask.render_template('home.html',cookies=cookies, is_admin = is_admin, is_authenticated = is_authenticated, is_name = is_name)
except Exception as error:
    print(error)